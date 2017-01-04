import logging
from op_service.service import OPService


logging.debug("Initializing service...")


# This module MUST expose the OPService object as the variable "service" (to work with uWSGI)
service = OPService()


logging.info("Initializing components...")


logging.warning("What follows is an empty line...\n\nThis line is not empty!")


logging.error("Initializing APIs...")


logging.critical("Initializing background workers...")


# These are components that show up in the dashboard as configurable dependencies
#class AbstractArivaleServiceComponent(object):
#
#  @abstract
#  def create(self, service_name):
#    pass
#
#class S3Component(AbstractArivaleServiceComponent):
#
#  def create(self, service_name):
#    # There's no need to create it an IAM account or anything - since it runs on EC2 host (both for staging and prod), it will use that instance policy (which right now is named "amazon-ecs-cli-setup-arivale-EcsInstancePolicy-6P6RYB326QT8" - gross). Actually, in the case of S3, I think there's literally nothing we need to do. We can connect directly.
#    pass
#
#  def get_json_description(self):
#    return
#
#class S3ComponentFactory(ArivaleServiceComponentFactory):
#
#  # A factory method that actually produces the thing (as a singleton)
#  @staticmethod
#  def build():
#    return boto.connect_s3()


# Add all the components
# Note: these are generally network dependencies and should ALL have staging vs. prod distinction (particularly RDS)
#service.add_component(aws_s3=boto.connect_s3())
#service.add_component(aws_sqs)
#service.add_component(aws_sns)
#service.add_component(aws_swf)
#service.add_component(aws_lambda)
#service.add_component(aws_rds_postgres)

# Make sure the service is "warmed up" (might mean different things in different stages)
# ...

# Import all the entry points
# Note: these entry points will have back-references to the "service", and background threads will start immediately, so
#   make sure everything is properly initialized by this point
from api import *
#from background import *

# At the end of this file, we now have a global "service" ArivaleService object we can export. You can start this via
# python using "serivce.start()" or via nginx / uwsgi by accessing the "service.flask_app" attribute.
