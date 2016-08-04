#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def affine_forward(x, w, b):
  """
  全连接层的前向运算实现

  The input x has shape (N, d_1, ..., d_k) where x[i] is the ith input.
  We multiply this against a weight matrix of shape (D, M) where
  D = \prod_i d_i

  Inputs:
  x - Input data, of shape (N, d_1, ..., d_k)
  w - Weights, of shape (D, M)
  b - Biases, of shape (M,)
  
  Returns a tuple of:
  - out: output, of shape (N, M)
  - cache: (x, w, b)
  """
  out = None

  # 对输入做reshape
  out = x.reshape( x.shape[0], np.prod(x.shape[1:]) )
  # 全连接计算 wx+b 
  out = out.dot(w) + b[np.newaxis, :]

  cache = (x, w, b)
  return out, cache


def affine_backward(dout, cache):
  """
  全连接层的反向传播计算

  Inputs:
  - dout: Upstream derivative, of shape (N, M)
  - cache: Tuple of:
    - x: Input data, of shape (N, d_1, ... d_k)
    - w: Weights, of shape (D, M)

  Returns a tuple of:
  - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
  - dw: Gradient with respect to w, of shape (D, M)
  - db: Gradient with respect to b, of shape (M,)
  """
  x, w, b = cache
  dx, dw, db = None, None, None

  sp = x.shape

  x  = np.reshape( x, ( sp[0] , np.prod(sp[1:]) ) )
  dw = np.dot( x.T, dout )
  db = np.sum( dout, axis=0 )
  dx = np.reshape( np.dot( dout, w.T ), sp )

  return dx, dw, db


def relu_forward(x):
  """
  ReLU激活层的前向计算

  Input:
  - x: Inputs, of any shape

  Returns a tuple of:
  - out: Output, of the same shape as x
  - cache: x
  """
  out = None

  out = x.copy()
  # ReLU激活
  out[out < 0] = 0

  cache = x
  return out, cache


def relu_backward(dout, cache):
  """
  ReLU层的反向传播实现

  Input:
  - dout: Upstream derivatives, of any shape
  - cache: Input x, of same shape as dout

  Returns:
  - dx: Gradient with respect to x
  """
  dx, x = None, cache

  dx = dout.copy()

  # ReLU的分段计算
  dx[x <= 0] = 0

  return dx


def conv_forward_naive(x, w, b, conv_param):
  """
  卷积层的前向运算

  The input consists of N data points, each with C channels, height H and width
  W. We convolve each input with F different filters, where each filter spans
  all C channels and has height HH and width HH.

  Input:
  - x: Input data of shape (N, C, H, W)
  - w: Filter weights of shape (F, C, HH, WW)
  - b: Biases, of shape (F,)
  - conv_param: A dictionary with the following keys:
    - 'stride': The number of pixels between adjacent receptive fields in the
      horizontal and vertical directions.
    - 'pad': The number of pixels that will be used to zero-pad the input.

  Returns a tuple of:
  - out: Output data, of shape (N, F, H', W') where H' and W' are given by
    H' = 1 + (H + 2 * pad - HH) / stride
    W' = 1 + (W + 2 * pad - WW) / stride
  - cache: (x, w, b, conv_param)
  """
  out = None

  N, C, H, W   = x.shape
  F, _, HH, WW = w.shape
  stride, pad  = conv_param['stride'], conv_param['pad']

  # 维度检测
  assert ( H + 2 * pad - HH) % stride == 0, 'width doesn\'t work with current paramter setting'
  assert ( W + 2 * pad - WW) % stride == 0, 'height doesn\'t work with current paramter setting'

  # 初始化输出
  out_H = ( H + 2 * pad - HH) / stride + 1
  out_W = ( W + 2 * pad - WW) / stride + 1
  out = np.zeros( (N, F, out_H, out_W), dtype=x.dtype ) 

  from im2col import im2col_indices

  x_cols = im2col_indices(x, HH, WW, padding=pad, stride=stride)

  res = w.reshape((w.shape[0], -1)).dot(x_cols) + b[:, np.newaxis]

  out = res.reshape((F, out_H, out_W, N))
  out = out.transpose(3, 0, 1, 2)

  cache = (x, w, b, conv_param, x_cols)
  return out, cache


def conv_backward_naive(dout, cache, debug=False):
  """
  卷积层的反向传播实现

  Inputs:
  - dout: Upstream derivatives.
  - cache: A tuple of (x, w, b, conv_param) as in conv_forward_naive

  Returns a tuple of:
  - dx: Gradient with respect to x
  - dw: Gradient with respect to w
  - db: Gradient with respect to b
  """

  dx, dw, db = None, None, None

  x, w, b, conv_param, x_cols = cache
  stride, pad = conv_param['stride'], conv_param['pad']

  db = np.sum( dout, axis=(0, 2, 3) )
  F, _, HH, WW = w.shape

  dout_reshape = np.reshape(dout.transpose(1,2,3,0), (F, -1))

  dw = dout_reshape.dot(x_cols.T).reshape(w.shape)

  dx_cols = w.reshape(F, -1).T.dot(dout_reshape)

  from im2col import col2im_indices

  dx = col2im_indices(dx_cols, x.shape, field_height=HH, field_width=WW, padding=pad, stride=stride, verbose=True)

  if debug:
    print "dout's shape: {}".format( str(dout.shape) ) 
    print "dout's reshape: {}".format( str(dout_reshape.shape))
    print "x's shape: {}".format( str(x.shape) )
    print "x's cols: {}".format( str(x_cols.shape))
    print "w's shape: {}".format( str(w.shape) )
    print "b's shape: {}".format( str(b.shape) )
    print "stride: {}".format( str(conv_param["stride"]) )
    print "padding: {}".format( str(conv_param["pad"]) )


  return dx, dw, db


def max_pool_forward_naive(x, pool_param):
  """
  最大池化层的前向运算

  Inputs:
  - x: Input data, of shape (N, C, H, W)
  - pool_param: dictionary with the following keys:
    - 'pool_height': The height of each pooling region
    - 'pool_width': The width of each pooling region
    - 'stride': The distance between adjacent pooling regions

  Returns a tuple of:
  - out: Output data
  - cache: (x, pool_param)
  """

  N, C, H, W = x.shape

  pool_height, pool_width, stride = pool_param['pool_height'], pool_param['pool_width'], pool_param['stride']

  # 确认窗口长宽是可以被整除的
  assert H % pool_height == 0, "Image height not divisible by pooling height"
  assert W % pool_width == 0, "Image width not divisible by pooling width"

  out = np.zeros((N, C, H / pool_height, W / pool_width))

  # 窗口滑动，逐个进行池化下采样
  for ii, i in enumerate(xrange(0, H, stride)):
    for jj, j in enumerate(xrange(0, W, stride)):
      # iterate through each central point
      out[:, :, ii, jj] = np.amax( x[:, :, i:i+pool_height,j:j+pool_width].reshape(N, C, -1), axis=2)

  cache = (x, pool_param)
  return out, cache


def max_pool_backward_naive(dout, cache):
  """
  最大池化层的反向运算

  Inputs:
  - dout: Upstream derivatives
  - cache: A tuple of (x, pool_param) as in the forward pass.

  Returns:
  - dx: Gradient with respect to x
  """

  # 取出x和池化的参数
  x, pool_param = cache

  N, C, H, W = x.shape
  pool_height, pool_width, stride = pool_param['pool_height'], pool_param['pool_width'], pool_param['stride']

  dx = np.zeros_like(x)
  # 池化层反向传播
  for ii, i in enumerate(xrange(0, H, stride)):
    for jj, j in enumerate(xrange(0, W, stride)):
      max_idx = np.argmax( x[:, :, i:i+pool_height,j:j+pool_width].reshape(N, C, -1), axis=2)

      max_cols = np.remainder(max_idx, pool_width) + j
      max_rows = max_idx / pool_width + i

      for n in xrange(N):
        for c in xrange(C):
          dx[n, c, max_rows[n, c], max_cols[n, c]] += dout[n, c, ii, jj]


  dx = dx.reshape(N, C, H, W)

  return dx


def svm_loss(x, y):
  """
  多分类的SVM计算损失和梯度

  Inputs:
  - x: Input data, of shape (N, C) where x[i, j] is the score for the jth class
    for the ith input.
  - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
    0 <= y[i] < C

  Returns a tuple of:
  - loss: Scalar giving the loss
  - dx: Gradient of the loss with respect to x
  """
  N = x.shape[0]
  correct_class_scores = x[np.arange(N), y]
  margins = np.maximum(0, x - correct_class_scores[:, np.newaxis] + 1.0)
  margins[np.arange(N), y] = 0
  loss = np.sum(margins) / N
  num_pos = np.sum(margins > 0, axis=1)
  dx = np.zeros_like(x)
  dx[margins > 0] = 1
  dx[np.arange(N), y] -= num_pos
  dx /= N
  return loss, dx


def softmax_loss(x, y):
  """
  多分类的softmax计算损失和梯度

  Inputs:
  - x: Input data, of shape (N, C) where x[i, j] is the score for the jth class
    for the ith input.
  - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
    0 <= y[i] < C

  Returns a tuple of:
  - loss: Scalar giving the loss
  - dx: Gradient of the loss with respect to x
  """
  probs = np.exp(x - np.max(x, axis=1, keepdims=True))
  probs /= np.sum(probs, axis=1, keepdims=True)
  N = x.shape[0]
  loss = -np.sum(np.log(probs[np.arange(N), y])) / N
  dx = probs.copy()
  dx[np.arange(N), y] -= 1
  dx /= N
  return loss, dx

