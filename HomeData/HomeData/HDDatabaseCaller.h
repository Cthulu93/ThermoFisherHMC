//
//  HDDatabaseCaller.h
//  HomeData
//
//  Created by Rupert Deese on 4/20/14.
//  Copyright (c) 2014 Rupert Deese. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <AWSDynamoDB/AWSDynamoDB.h>
#import "Constants.h"

static AmazonDynamoDBClient *ddb = nil;

@interface HDDatabaseCaller : NSObject

+(void)initClientsWithEmbeddedCredentials;

+ (NSMutableArray*) getTHLDataForTimeBegin:(NSDate*) begin andEnd:(NSDate*) end withResolution:(NSString*) res;

+(AmazonDynamoDBClient *)ddb;

@end
