/*
 * Copyright 2010-2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

#define TEST_TABLE_NAME              @"TestUserPreference"
#define TEST_TABLE_HASH_KEY          @"userNo"

#define TABLE_NAME @"raspi"

//Fill in these two fields to bypass WIF
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
#define ACCESS_KEY_ID                @"AKIAIJ3V2Q6QO4NXO7VA"
#define SECRET_KEY                   @"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"


@interface Constants:NSObject
{
}

@end
