//
//  HDHomeViewController.h
//  HomeData
//
//  Created by Rupert Deese on 4/20/14.
//  Copyright (c) 2014 Rupert Deese. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "JBLineChartView.h"
#import "HDDatabaseCaller.h"

@interface HDHomeViewController : UIViewController <JBLineChartViewDataSource, JBLineChartViewDelegate>

@property IBOutlet JBLineChartView *temp;
@property IBOutlet JBLineChartView *hum;
@property IBOutlet JBLineChartView *light;
@property IBOutlet UILabel *label;
@property NSMutableArray *chartData;

@end
