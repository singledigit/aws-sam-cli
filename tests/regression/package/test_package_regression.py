from unittest import skipIf
from parameterized import parameterized

from .regression_package_base import PackageRegressionBase
from tests.testing_utils import RUNNING_ON_CI, RUNNING_TEST_FOR_MASTER_ON_CI

# Package Regression tests require credentials and CI/CD will only add credentials to the env if the PR is from the same repo.
# This is to restrict package tests to run outside of CI/CD and when the branch is not master.
SKIP_PACKAGE_REGRESSION_TESTS = RUNNING_ON_CI and RUNNING_TEST_FOR_MASTER_ON_CI


# Only tested cases where the output template file changes, adding metadata or kms keys does not change the output.


@skipIf(SKIP_PACKAGE_REGRESSION_TESTS, "Skip package regression tests in CI/CD only")
class TestPackageRegression(PackageRegressionBase):
    def setUp(self):
        super(TestPackageRegression, self).setUp()

    def tearDown(self):
        super(TestPackageRegression, self).tearDown()

    @parameterized.expand(
        [
            "aws-serverless-function.yaml",
            "aws-serverless-api.yaml",
            "aws-appsync-graphqlschema.yaml",
            "aws-appsync-resolver.yaml",
            "aws-appsync-functionconfiguration.yaml",
            "aws-lambda-function.yaml",
            "aws-apigateway-restapi.yaml",
            "aws-elasticbeanstalk-applicationversion.yaml",
            "aws-cloudformation-stack.yaml",
            "aws-serverless-application.yaml",
            "aws-lambda-layerversion.yaml",
            "aws-serverless-layerversion.yaml",
            "aws-glue-job.yaml",
            "aws-serverlessrepo-application.yaml",
        ]
    )
    def test_package_with_output_template_file(self, template_file):

        arguments = {"s3_bucket": self.s3_bucket.name, "template_file": self.test_data_path.joinpath(template_file)}

        self.regression_check(arguments)

    @parameterized.expand(
        [
            "aws-serverless-function.yaml",
            "aws-serverless-api.yaml",
            "aws-appsync-graphqlschema.yaml",
            "aws-appsync-resolver.yaml",
            "aws-appsync-functionconfiguration.yaml",
            "aws-lambda-function.yaml",
            "aws-apigateway-restapi.yaml",
            "aws-elasticbeanstalk-applicationversion.yaml",
            "aws-cloudformation-stack.yaml",
            "aws-serverless-application.yaml",
            "aws-lambda-layerversion.yaml",
            "aws-serverless-layerversion.yaml",
            "aws-glue-job.yaml",
            "aws-serverlessrepo-application.yaml",
        ]
    )
    def test_package_with_output_template_file_and_prefix(self, template_file):

        arguments = {
            "s3_bucket": self.s3_bucket.name,
            "template_file": self.test_data_path.joinpath(template_file),
            "s3_prefix": "regression/tests",
        }

        self.regression_check(arguments)

    @parameterized.expand(
        [
            "aws-serverless-function.yaml",
            "aws-serverless-api.yaml",
            "aws-appsync-graphqlschema.yaml",
            "aws-appsync-resolver.yaml",
            "aws-appsync-functionconfiguration.yaml",
            "aws-lambda-function.yaml",
            "aws-apigateway-restapi.yaml",
            "aws-elasticbeanstalk-applicationversion.yaml",
            "aws-cloudformation-stack.yaml",
            "aws-serverless-application.yaml",
            "aws-lambda-layerversion.yaml",
            "aws-serverless-layerversion.yaml",
            "aws-glue-job.yaml",
            "aws-serverlessrepo-application.yaml",
        ]
    )
    def test_package_with_output_template_file_json_and_prefix(self, template_file):

        arguments = {
            "s3_bucket": self.s3_bucket.name,
            "template_file": self.test_data_path.joinpath(template_file),
            "s3_prefix": "regression/tests",
            "use_json": True,
        }

        self.regression_check(arguments)
