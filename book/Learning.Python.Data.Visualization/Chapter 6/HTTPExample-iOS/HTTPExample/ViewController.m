//
//  ViewController.m
//  HTTPExample
//
//  Created by Chad Adams on 6/2/14.
//  Copyright (c) 2014 Chad Adams. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UITextView *output;

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    NSURL *packtURL = [NSURL URLWithString:@"http://www.packtpub.com/rss.xml"];
    
    
    NSURLRequest *request = [NSURLRequest requestWithURL:packtURL];
    
    NSURLConnection *connection = [[NSURLConnection alloc] initWithRequest:request delegate:self startImmediately:YES];
    
    [connection start];
}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
    NSString *downloadstring = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
    
    [self.output setText:downloadstring];
    
}


- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
