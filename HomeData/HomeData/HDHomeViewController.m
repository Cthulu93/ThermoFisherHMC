

//  HDHomeViewController.m
//  HomeData
//
//  Created by Rupert Deese on 4/20/14.
//  Copyright (c) 2014 Rupert Deese. All rights reserved.
//

#import "HDHomeViewController.h"

@interface HDHomeViewController ()
@property float fWidth, fHeight;
@end

@implementation HDHomeViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
        [HDDatabaseCaller initClientsWithEmbeddedCredentials];
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    _fWidth = self.view.frame.size.width;
    _fHeight = self.view.frame.size.width;
    
    _chartData = [HDDatabaseCaller getTHLDataForTimeBegin:[NSDate dateWithTimeIntervalSinceNow:-600]  andEnd:[NSDate date] withResolution:@"minute_average"];
    
//    _temp = [[JBLineChartView alloc] initWithFrame:CGRectMake(0.2*_fWidth, 0.2*_fHeight, 0.6*_fWidth, 0.6*_fHeight)];
    
    _temp.delegate = self;
    _temp.dataSource = self;
    [self.view addSubview:_temp];
    [_temp setTag:42];
    [_temp reloadData];
    
    _hum.delegate = self;
    _hum.dataSource = self;
    [_hum setTag:43];
    [self.view addSubview:_hum];
    [_hum reloadData];
    
    _light.delegate = self;
    _light.dataSource = self;
    [_light setTag:44];
    [self.view addSubview:_light];
    [_light reloadData];
    
    [NSTimer timerWithTimeInterval:30.0 target:self selector:<#(SEL)#> userInfo:<#(id)#> repeats:<#(BOOL)#>]
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void) reload {
    [_temp reloadData];
}

- (NSUInteger)numberOfLinesInLineChartView:(JBLineChartView *)lineChartView
{
    return  1; // number of lines in chart
}

- (NSUInteger)lineChartView:(JBLineChartView *)lineChartView numberOfVerticalValuesAtLineIndex:(NSUInteger)lineIndex
{
    return [_chartData count]; // number of values for a line
}

- (CGFloat)lineChartView:(JBLineChartView *)lineChartView verticalValueForHorizontalIndex:(NSUInteger)horizontalIndex atLineIndex:(NSUInteger)lineIndex
{
    NSString *key;
    if ([lineChartView tag] == 42) key = @"temperature";
    if ([lineChartView tag] == 43) key = @"humidity";
    if ([lineChartView tag] == 44) key = @"light";
        
    DynamoDBAttributeValue *dict = [[_chartData objectAtIndex:horizontalIndex] valueForKey:key];
    if (dict) {
        NSLog(@"%f", [[dict n] floatValue]);
        return [[dict n] floatValue];
    }
    else return 0;
}

- (void) lineChartView:(JBLineChartView *)lineChartView didSelectLineAtIndex:(NSUInteger)lineIndex horizontalIndex:(NSUInteger)horizontalIndex {
    
    DynamoDBAttributeValue *dict = [[_chartData objectAtIndex:horizontalIndex] valueForKey:@"date"];
    
    NSTimeInterval _interval= [[dict n] floatValue];
    NSDate *date = [NSDate dateWithTimeIntervalSince1970:_interval];
    NSDateFormatter *_formatter=[[NSDateFormatter alloc]init];
    [_formatter setLocale:[NSLocale currentLocale]];
    [_formatter setDateFormat:@"HH:mm:ss"];
    NSString *dstring =[_formatter stringFromDate:date];
    
    if ([lineChartView tag] == 42) {
        [_label setText:[NSString stringWithFormat:@"%@ -- %f", dstring, [self lineChartView:lineChartView verticalValueForHorizontalIndex:horizontalIndex atLineIndex:0]]];
    }
}
@end
