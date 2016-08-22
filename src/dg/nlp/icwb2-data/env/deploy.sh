For Win
python scripts\dw.py training\pku_training.utf8 testing\pku_test.utf8 pku_result.utf8
perl scripts\score training\pku_training.utf8 gold\pku_test_gold.utf8 pku_result.utf8 > score.utf8

For Ubuntu
python ./scripts/dw.py ./training/pku_training.utf8 ./testing/pku_test.utf8 ./result/pku_result.utf8
perl ./scripts/score ./training/pku_training.utf8 ./gold/pku_test_gold.utf8 ./result/pku_result.utf8 > ./result/score.utf8
tail ./result/score.utf8

tar -zxvf CRF++-0.58.tar.gz
cd CRF++-0.58

# configure & make & (sudo) make install
./configure
make
sudo make install

# install python-dev
sudo apt-get install python-dev
cd python
python setup.py build
sudo python setup.py install
mkdir crf++
python ./scripts/make_crf_train_data.py ./training/pku_training.utf8 ./crf++/pku_training.tagging4crf.utf8
# python ./scripts/make_crf_test_data.py ./testing/pku_test.utf8 /crf++/pku_test4crf.utf8
python ./scripts/make_crf_test_data.py ./testing/pku_test.utf8 ./crf++/pku_test4crf.utf8
# crf_learn -f 3 -c 4.0 template ./crf++/pku_training.tagging4crf.utf8 crf_model
crf_learn -f 3 -c 4.0 ~/Documents/workspace/CRF++-0.58/example/seg/template ./crf++/pku_training.tagging4crf.utf8 ./crf++/crf_model

crf_test -m ./crf++/crf_model ./crf++/pku_test4crf.utf8 > ./crf++/pku_test4crf.tag.utf8
python ./scripts/crf_data_2_word.py ./crf++/pku_test4crf.tag.utf8 ./crf++/pku_test4crf.tag2word.utf8
perl ./scripts/score ./training/pku_training.utf8 ./gold/pku_test_gold.utf8 ./crf++/pku_test4crf.tag2word.utf8 > ./crf++/score.utf8
tail ./crf++/score.utf8

