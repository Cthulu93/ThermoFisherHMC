//
//  HDDatabaseCaller.m
//  HomeData
//
//  Created by Rupert Deese on 4/20/14.
//  Copyright (c) 2014 Rupert Deese. All rights reserved.
//

#import "HDDatabaseCaller.h"

@implementation HDDatabaseCaller

+ (NSMutableArray*) getTHLDataForTimeBegin:(NSDate*) begin andEnd:(NSDate*) end withResolution:(NSString*) res {
    DynamoDBQueryRequest *request = [[DynamoDBQueryRequest alloc] initWithTableName:TABLE_NAME];
    DynamoDBCondition *hashEq = [DynamoDBCondition new];
    hashEq.comparisonOperator = @"EQ";
    DynamoDBAttributeValue *station = [[DynamoDBAttributeValue alloc] initWithS:res];
    [hashEq addAttributeValueList:station];
    
    DynamoDBCondition *dateBw = [DynamoDBCondition new];
    dateBw.comparisonOperator = @"BETWEEN";
    DynamoDBAttributeValue *start = [[DynamoDBAttributeValue alloc] initWithN:[NSString stringWithFormat:@"%f",[begin timeIntervalSince1970]]];
    DynamoDBAttributeValue *finish = [[DynamoDBAttributeValue alloc] initWithN:[NSString stringWithFormat:@"%f",[end timeIntervalSince1970]]];
    [dateBw addAttributeValueList:start];
    [dateBw addAttributeValueList:finish];
    
    request.keyConditions = [NSMutableDictionary dictionaryWithObjectsAndKeys:hashEq, @"station", dateBw, @"date", nil];
    
    DynamoDBQueryResponse *response = [ddb query:request];
    
    if(response.error != nil)
    {
        NSLog(@"Error: %@", response.error);
        
        return nil;
    }
    else {
        NSLog(@"Description: %@", response.description);
    }
    
    return response.items;
}

//+(NSMutableArray *)getUserList
//{
//    DynamoDBScanRequest  *request  = [[DynamoDBScanRequest alloc] initWithTableName:TABLE_NAME];
//    DynamoDBScanResponse *response = [ddb scan:request];
//    if(response.error != nil)
//    {
//        NSLog(@"Error: %@", response.error);
//        
//        return nil;
//    }
//    
//    return response.items;
//}

+(void)initClientsWithEmbeddedCredentials
{
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // This sample App is for demonstration purposes only.
    // It is not secure to embed your credentials into source code.
    // DO NOT EMBED YOUR CREDENTIALS IN PRODUCTION APPS.
    // We offer two solutions for getting credentials to your mobile App.
    // Please read the following article to learn about Token Vending Machine:
    // * http://aws.amazon.com/articles/Mobile/4611615499399490
    // Or consider using web identity federation:
    // * http://aws.amazon.com/articles/Mobile/4617974389850313
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if (ddb == nil) {
        AmazonCredentials *credentials = [[AmazonCredentials alloc] initWithAccessKey:ACCESS_KEY_ID withSecretKey:SECRET_KEY];
        ddb = [[AmazonDynamoDBClient alloc] initWithCredentials:credentials];
    }
}

+(AmazonDynamoDBClient *)ddb
{
    return ddb;
}

/*
 * Retrieves the table description and returns the table status as a string.
 */
+(NSString *)getTestTableStatus
{
    DynamoDBDescribeTableRequest  *request  = [[DynamoDBDescribeTableRequest alloc] initWithTableName:TEST_TABLE_NAME];
    DynamoDBDescribeTableResponse *response = [ddb describeTable:request];
    if(response.error != nil)
    {
        if([[response.error.userInfo objectForKey:@"exception"] isKindOfClass:[DynamoDBResourceNotFoundException class]])
        {
            return nil;
        }
        
        NSLog(@"Error: %@", response.error);
        
        return nil;
    }
    
    return response.table.tableStatus;
}

@end
