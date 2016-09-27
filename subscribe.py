import boto3

client = boto3.client('sns')


def subscribe(number, location):
    switcher = {
        '0': 'arn:aws:sns:us-west-2:152022601810:C3_Menu',
        '1': 'arn:aws:sns:us-west-2:152022601810:MS_Menu',
        '2': 'arn:aws:sns:us-west-2:152022601810:GOV_Menu',
    }

    response = client.subscribe(
        TopicArn=switcher.get(location, 'FAIL'),
        Protocol='sms',
        Endpoint=number
    )

numbers = raw_input("Phone number: ")
locations = raw_input(
    "\n0 for Crossroads Culinary Center\n1 for Main Street Market Dining Center\n2 for Governors Dining Center\n\nWhich one? ")
subscribe(numbers, locations)
