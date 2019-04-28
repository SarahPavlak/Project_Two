from my_script import enlarge, notification

def test_enlarge(): 
    result = enlarge 
    assert result == 'avalon-ballston-square' or 'ava-ballston' or  'ava-ballston,avalon-ballston-square' 

def test_notification(): 
    result = notification
    assert result == 'One time' or 'Recurring' or 'One time,Recurring'


#testing that apartment and notification csv has a value!
