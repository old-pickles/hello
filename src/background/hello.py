from functools import wraps
from service import service



import time
def interval(time_s):
  def decorator(f):
    @wraps(f)
    def target():
      while True:
        try:
          f()
        except:
          logger.exception("Periodic background process threw exception")
        time.sleep(time_s)
    return target
  return decorator



@service.background()
@interval(3)
def print_hello():
  """
  This function runs periodically and prints a message
  """
  print "Hello from background/hello.py"





# https://startupnextdoor.com/adding-to-sqs-queue-using-aws-lambda-and-a-serverless-api-endpoint/

# http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html

# http://boto3.readthedocs.io/en/latest/reference/services/lambda.html#Lambda.Client.create_function

# TODO: eventually you should enable these lambda functions to be automatically created / updated
# @service.background()
# @service.components.sqs.queue_message_handler()
