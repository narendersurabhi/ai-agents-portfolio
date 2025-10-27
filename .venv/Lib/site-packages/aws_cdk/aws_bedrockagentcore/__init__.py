r'''
# AWS::BedrockAgentCore Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_bedrockagentcore as bedrockagentcore
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BedrockAgentCore construct libraries](https://constructs.dev/search?q=bedrockagentcore)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BedrockAgentCore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BedrockAgentCore.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BedrockAgentCore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BedrockAgentCore.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.BrowserCustomReference",
    jsii_struct_bases=[],
    name_mapping={"browser_id": "browserId"},
)
class BrowserCustomReference:
    def __init__(self, *, browser_id: builtins.str) -> None:
        '''A reference to a BrowserCustom resource.

        :param browser_id: The BrowserId of the BrowserCustom resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            browser_custom_reference = bedrockagentcore.BrowserCustomReference(
                browser_id="browserId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e545da2b3da370563839cf7802f81e77f186bac4ddee7d944e49364fcf8806)
            check_type(argname="argument browser_id", value=browser_id, expected_type=type_hints["browser_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "browser_id": browser_id,
        }

    @builtins.property
    def browser_id(self) -> builtins.str:
        '''The BrowserId of the BrowserCustom resource.'''
        result = self._values.get("browser_id")
        assert result is not None, "Required property 'browser_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrowserCustomReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustomProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_configuration": "networkConfiguration",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "recording_config": "recordingConfig",
        "tags": "tags",
    },
)
class CfnBrowserCustomProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.BrowserNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBrowserCustom``.

        :param name: The name of the custom browser.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param description: The custom browser.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param recording_config: THe custom browser configuration.
        :param tags: The tags for the custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_browser_custom_props = bedrockagentcore.CfnBrowserCustomProps(
                name="name",
                network_configuration=bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                    network_mode="networkMode",
            
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                ),
            
                # the properties below are optional
                description="description",
                execution_role_arn="executionRoleArn",
                recording_config=bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                    enabled=False,
                    s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix"
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08f9adb5e20b52bbdc47438decbd54e3ebb4b1976cbf46432a19597fc6589c39)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument recording_config", value=recording_config, expected_type=type_hints["recording_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if recording_config is not None:
            self._values["recording_config"] = recording_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.

        This structure defines how the code interpreter connects to the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]]:
        '''THe custom browser configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-recordingconfig
        '''
        result = self._values.get("recording_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBrowserCustomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustomProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_configuration": "networkConfiguration",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "tags": "tags",
    },
)
class CfnCodeInterpreterCustomProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCodeInterpreterCustom``.

        :param name: The name of the code interpreter.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param description: The code interpreter description.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param tags: The tags for the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_code_interpreter_custom_props = bedrockagentcore.CfnCodeInterpreterCustomProps(
                name="name",
                network_configuration=bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                    network_mode="networkMode",
            
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                ),
            
                # the properties below are optional
                description="description",
                execution_role_arn="executionRoleArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5217aa9ccd0ec964b92c3a48855bb1494914c435606fcee5b0faefd790d264)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.

        This structure defines how the code interpreter connects to the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The code interpreter description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeInterpreterCustomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_type": "authorizerType",
        "name": "name",
        "protocol_type": "protocolType",
        "role_arn": "roleArn",
        "authorizer_configuration": "authorizerConfiguration",
        "description": "description",
        "exception_level": "exceptionLevel",
        "kms_key_arn": "kmsKeyArn",
        "protocol_configuration": "protocolConfiguration",
        "tags": "tags",
    },
)
class CfnGatewayProps:
    def __init__(
        self,
        *,
        authorizer_type: builtins.str,
        name: builtins.str,
        protocol_type: builtins.str,
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        exception_level: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        protocol_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GatewayProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGateway``.

        :param authorizer_type: The authorizer type for the gateway.
        :param name: The name for the gateway.
        :param protocol_type: The protocol type for the gateway target.
        :param role_arn: 
        :param authorizer_configuration: 
        :param description: The description for the gateway.
        :param exception_level: The exception level for the gateway.
        :param kms_key_arn: The KMS key ARN for the gateway.
        :param protocol_configuration: The protocol configuration for the gateway target.
        :param tags: The tags for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_gateway_props = bedrockagentcore.CfnGatewayProps(
                authorizer_type="authorizerType",
                name="name",
                protocol_type="protocolType",
                role_arn="roleArn",
            
                # the properties below are optional
                authorizer_configuration=bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
            
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"]
                    )
                ),
                description="description",
                exception_level="exceptionLevel",
                kms_key_arn="kmsKeyArn",
                protocol_configuration=bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty(
                    mcp=bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                        instructions="instructions",
                        search_type="searchType",
                        supported_versions=["supportedVersions"]
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790df6c55e75e75d6f8c8a9a5518586d5e4ae350e3bfc4555e2ed4bf3c572f31)
            check_type(argname="argument authorizer_type", value=authorizer_type, expected_type=type_hints["authorizer_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol_type", value=protocol_type, expected_type=type_hints["protocol_type"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument authorizer_configuration", value=authorizer_configuration, expected_type=type_hints["authorizer_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exception_level", value=exception_level, expected_type=type_hints["exception_level"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_type": authorizer_type,
            "name": name,
            "protocol_type": protocol_type,
            "role_arn": role_arn,
        }
        if authorizer_configuration is not None:
            self._values["authorizer_configuration"] = authorizer_configuration
        if description is not None:
            self._values["description"] = description
        if exception_level is not None:
            self._values["exception_level"] = exception_level
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if protocol_configuration is not None:
            self._values["protocol_configuration"] = protocol_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def authorizer_type(self) -> builtins.str:
        '''The authorizer type for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-authorizertype
        '''
        result = self._values.get("authorizer_type")
        assert result is not None, "Required property 'authorizer_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol_type(self) -> builtins.str:
        '''The protocol type for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-protocoltype
        '''
        result = self._values.get("protocol_type")
        assert result is not None, "Required property 'protocol_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.AuthorizerConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-authorizerconfiguration
        '''
        result = self._values.get("authorizer_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.AuthorizerConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exception_level(self) -> typing.Optional[builtins.str]:
        '''The exception level for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-exceptionlevel
        '''
        result = self._values.get("exception_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The KMS key ARN for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayProtocolConfigurationProperty"]]:
        '''The protocol configuration for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-protocolconfiguration
        '''
        result = self._values.get("protocol_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayProtocolConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "credential_provider_configurations": "credentialProviderConfigurations",
        "name": "name",
        "target_configuration": "targetConfiguration",
        "description": "description",
        "gateway_identifier": "gatewayIdentifier",
    },
)
class CfnGatewayTargetProps:
    def __init__(
        self,
        *,
        credential_provider_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.CredentialProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        target_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        gateway_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGatewayTarget``.

        :param credential_provider_configurations: The OAuth credential provider configuration.
        :param name: The name for the gateway target.
        :param target_configuration: The target configuration for the Smithy model target.
        :param description: The description for the gateway target.
        :param gateway_identifier: The gateway ID for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
            
            cfn_gateway_target_props = bedrockagentcore.CfnGatewayTargetProps(
                credential_provider_configurations=[bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty(
                    credential_provider_type="credentialProviderType",
            
                    # the properties below are optional
                    credential_provider=bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                        api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                            provider_arn="providerArn",
            
                            # the properties below are optional
                            credential_location="credentialLocation",
                            credential_parameter_name="credentialParameterName",
                            credential_prefix="credentialPrefix"
                        ),
                        oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                            provider_arn="providerArn",
                            scopes=["scopes"],
            
                            # the properties below are optional
                            custom_parameters={
                                "custom_parameters_key": "customParameters"
                            }
                        )
                    )
                )],
                name="name",
                target_configuration=bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty(
                    mcp=bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                        lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                            lambda_arn="lambdaArn",
                            tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                                inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                    description="description",
                                    input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
            
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    ),
                                    name="name",
            
                                    # the properties below are optional
                                    output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
            
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    )
                                )],
                                s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                    bucket_owner_account_id="bucketOwnerAccountId",
                                    uri="uri"
                                )
                            )
                        ),
                        open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        ),
                        smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    )
                ),
            
                # the properties below are optional
                description="description",
                gateway_identifier="gatewayIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367178269f9a78c89b5ba5e07b10a309050b4b3eaefd55c5ee6f30ddad20209f)
            check_type(argname="argument credential_provider_configurations", value=credential_provider_configurations, expected_type=type_hints["credential_provider_configurations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_configuration", value=target_configuration, expected_type=type_hints["target_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument gateway_identifier", value=gateway_identifier, expected_type=type_hints["gateway_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "credential_provider_configurations": credential_provider_configurations,
            "name": name,
            "target_configuration": target_configuration,
        }
        if description is not None:
            self._values["description"] = description
        if gateway_identifier is not None:
            self._values["gateway_identifier"] = gateway_identifier

    @builtins.property
    def credential_provider_configurations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]:
        '''The OAuth credential provider configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfigurations
        '''
        result = self._values.get("credential_provider_configurations")
        assert result is not None, "Required property 'credential_provider_configurations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.TargetConfigurationProperty"]:
        '''The target configuration for the Smithy model target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-targetconfiguration
        '''
        result = self._values.get("target_configuration")
        assert result is not None, "Required property 'target_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.TargetConfigurationProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_identifier(self) -> typing.Optional[builtins.str]:
        '''The gateway ID for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-gatewayidentifier
        '''
        result = self._values.get("gateway_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_expiry_duration": "eventExpiryDuration",
        "name": "name",
        "description": "description",
        "encryption_key_arn": "encryptionKeyArn",
        "memory_execution_role_arn": "memoryExecutionRoleArn",
        "memory_strategies": "memoryStrategies",
        "tags": "tags",
    },
)
class CfnMemoryProps:
    def __init__(
        self,
        *,
        event_expiry_duration: jsii.Number,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        memory_execution_role_arn: typing.Optional[builtins.str] = None,
        memory_strategies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.MemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMemory``.

        :param event_expiry_duration: The event expiry configuration.
        :param name: The memory name.
        :param description: Description of the Memory resource.
        :param encryption_key_arn: The memory encryption key Amazon Resource Name (ARN).
        :param memory_execution_role_arn: The memory role ARN.
        :param memory_strategies: The memory strategies.
        :param tags: The tags for the resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_memory_props = bedrockagentcore.CfnMemoryProps(
                event_expiry_duration=123,
                name="name",
            
                # the properties below are optional
                description="description",
                encryption_key_arn="encryptionKeyArn",
                memory_execution_role_arn="memoryExecutionRoleArn",
                memory_strategies=[bedrockagentcore.CfnMemory.MemoryStrategyProperty(
                    custom_memory_strategy=bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                            self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                                historical_context_window_size=123,
                                invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                    payload_delivery_bucket_name="payloadDeliveryBucketName",
                                    topic_arn="topicArn"
                                ),
                                trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                    message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                        message_count=123
                                    ),
                                    time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                        idle_session_timeout=123
                                    ),
                                    token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                        token_count=123
                                    )
                                )]
                            ),
                            semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            )
                        ),
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    semantic_memory_strategy=bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    summary_memory_strategy=bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    user_preference_memory_strategy=bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    )
                )],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28dda218e5909d8e89c4ab4ee9bac6335e1f1cde1c399e1ac3c1c739ece89e19)
            check_type(argname="argument event_expiry_duration", value=event_expiry_duration, expected_type=type_hints["event_expiry_duration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument memory_execution_role_arn", value=memory_execution_role_arn, expected_type=type_hints["memory_execution_role_arn"])
            check_type(argname="argument memory_strategies", value=memory_strategies, expected_type=type_hints["memory_strategies"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_expiry_duration": event_expiry_duration,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            self._values["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            self._values["memory_strategies"] = memory_strategies
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def event_expiry_duration(self) -> jsii.Number:
        '''The event expiry configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-eventexpiryduration
        '''
        result = self._values.get("event_expiry_duration")
        assert result is not None, "Required property 'event_expiry_duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The memory name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the Memory resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The memory encryption key Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The memory role ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-memoryexecutionrolearn
        '''
        result = self._values.get("memory_execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_strategies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.MemoryStrategyProperty"]]]]:
        '''The memory strategies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-memorystrategies
        '''
        result = self._values.get("memory_strategies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.MemoryStrategyProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_runtime_id": "agentRuntimeId",
        "name": "name",
        "agent_runtime_version": "agentRuntimeVersion",
        "description": "description",
        "tags": "tags",
    },
)
class CfnRuntimeEndpointProps:
    def __init__(
        self,
        *,
        agent_runtime_id: builtins.str,
        name: builtins.str,
        agent_runtime_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuntimeEndpoint``.

        :param agent_runtime_id: The agent runtime ID.
        :param name: The name of the AgentCore Runtime endpoint.
        :param agent_runtime_version: The version of the agent.
        :param description: Contains information about an agent runtime endpoint. An agent runtime is the execution environment for a Amazon Bedrock Agent.
        :param tags: The tags for the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_runtime_endpoint_props = bedrockagentcore.CfnRuntimeEndpointProps(
                agent_runtime_id="agentRuntimeId",
                name="name",
            
                # the properties below are optional
                agent_runtime_version="agentRuntimeVersion",
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03746d507f3e8e95afbebc436c73d1ac1fc643ccea60f817b99b76cb41ccf5fb)
            check_type(argname="argument agent_runtime_id", value=agent_runtime_id, expected_type=type_hints["agent_runtime_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument agent_runtime_version", value=agent_runtime_version, expected_type=type_hints["agent_runtime_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_id": agent_runtime_id,
            "name": name,
        }
        if agent_runtime_version is not None:
            self._values["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_runtime_id(self) -> builtins.str:
        '''The agent runtime ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-agentruntimeid
        '''
        result = self._values.get("agent_runtime_id")
        assert result is not None, "Required property 'agent_runtime_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_runtime_version(self) -> typing.Optional[builtins.str]:
        '''The version of the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-agentruntimeversion
        '''
        result = self._values.get("agent_runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Contains information about an agent runtime endpoint.

        An agent runtime is the execution environment for a Amazon Bedrock Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuntimeEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_runtime_artifact": "agentRuntimeArtifact",
        "agent_runtime_name": "agentRuntimeName",
        "network_configuration": "networkConfiguration",
        "role_arn": "roleArn",
        "authorizer_configuration": "authorizerConfiguration",
        "description": "description",
        "environment_variables": "environmentVariables",
        "protocol_configuration": "protocolConfiguration",
        "tags": "tags",
    },
)
class CfnRuntimeProps:
    def __init__(
        self,
        *,
        agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AgentRuntimeArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
        agent_runtime_name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        protocol_configuration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuntime``.

        :param agent_runtime_artifact: The artifact of the agent.
        :param agent_runtime_name: The name of the AgentCore Runtime endpoint.
        :param network_configuration: The network configuration.
        :param role_arn: The Amazon Resource Name (ARN) for for the role.
        :param authorizer_configuration: Represents inbound authorization configuration options used to authenticate incoming requests.
        :param description: The agent runtime description.
        :param environment_variables: The environment variables for the agent.
        :param protocol_configuration: The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.
        :param tags: The tags for the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_runtime_props = bedrockagentcore.CfnRuntimeProps(
                agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                    container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                        container_uri="containerUri"
                    )
                ),
                agent_runtime_name="agentRuntimeName",
                network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                    network_mode="networkMode",
            
                    # the properties below are optional
                    network_mode_config=bedrockagentcore.CfnRuntime.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
            
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"]
                    )
                ),
                description="description",
                environment_variables={
                    "environment_variables_key": "environmentVariables"
                },
                protocol_configuration="protocolConfiguration",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e489b12cef85647a902e6bba6db3bf5f3ef1a856b74cf0fc5a7f8d1d0fa4a4b)
            check_type(argname="argument agent_runtime_artifact", value=agent_runtime_artifact, expected_type=type_hints["agent_runtime_artifact"])
            check_type(argname="argument agent_runtime_name", value=agent_runtime_name, expected_type=type_hints["agent_runtime_name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument authorizer_configuration", value=authorizer_configuration, expected_type=type_hints["authorizer_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_artifact": agent_runtime_artifact,
            "agent_runtime_name": agent_runtime_name,
            "network_configuration": network_configuration,
            "role_arn": role_arn,
        }
        if authorizer_configuration is not None:
            self._values["authorizer_configuration"] = authorizer_configuration
        if description is not None:
            self._values["description"] = description
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if protocol_configuration is not None:
            self._values["protocol_configuration"] = protocol_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_runtime_artifact(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"]:
        '''The artifact of the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-agentruntimeartifact
        '''
        result = self._values.get("agent_runtime_artifact")
        assert result is not None, "Required property 'agent_runtime_artifact' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"], result)

    @builtins.property
    def agent_runtime_name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-agentruntimename
        '''
        result = self._values.get("agent_runtime_name")
        assert result is not None, "Required property 'agent_runtime_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"]:
        '''The network configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for for the role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]]:
        '''Represents inbound authorization configuration options used to authenticate incoming requests.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-authorizerconfiguration
        '''
        result = self._values.get("authorizer_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The agent runtime description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''The environment variables for the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-environmentvariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def protocol_configuration(self) -> typing.Optional[builtins.str]:
        '''The protocol configuration for an agent runtime.

        This structure defines how the agent runtime communicates with clients.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-protocolconfiguration
        '''
        result = self._values.get("protocol_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuntimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CodeInterpreterCustomReference",
    jsii_struct_bases=[],
    name_mapping={"code_interpreter_id": "codeInterpreterId"},
)
class CodeInterpreterCustomReference:
    def __init__(self, *, code_interpreter_id: builtins.str) -> None:
        '''A reference to a CodeInterpreterCustom resource.

        :param code_interpreter_id: The CodeInterpreterId of the CodeInterpreterCustom resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            code_interpreter_custom_reference = bedrockagentcore.CodeInterpreterCustomReference(
                code_interpreter_id="codeInterpreterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89dc37aef7efb202707ab991eff3008383de6de10f2228d9e9beb350d3f170d5)
            check_type(argname="argument code_interpreter_id", value=code_interpreter_id, expected_type=type_hints["code_interpreter_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_interpreter_id": code_interpreter_id,
        }

    @builtins.property
    def code_interpreter_id(self) -> builtins.str:
        '''The CodeInterpreterId of the CodeInterpreterCustom resource.'''
        result = self._values.get("code_interpreter_id")
        assert result is not None, "Required property 'code_interpreter_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeInterpreterCustomReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.GatewayReference",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_arn": "gatewayArn",
        "gateway_identifier": "gatewayIdentifier",
    },
)
class GatewayReference:
    def __init__(
        self,
        *,
        gateway_arn: builtins.str,
        gateway_identifier: builtins.str,
    ) -> None:
        '''A reference to a Gateway resource.

        :param gateway_arn: The ARN of the Gateway resource.
        :param gateway_identifier: The GatewayIdentifier of the Gateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            gateway_reference = bedrockagentcore.GatewayReference(
                gateway_arn="gatewayArn",
                gateway_identifier="gatewayIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4e6eebff32fea6f708a0bdf21025e0a9500bd2a3cdfdda828c784ebacee92ec)
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
            check_type(argname="argument gateway_identifier", value=gateway_identifier, expected_type=type_hints["gateway_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_arn": gateway_arn,
            "gateway_identifier": gateway_identifier,
        }

    @builtins.property
    def gateway_arn(self) -> builtins.str:
        '''The ARN of the Gateway resource.'''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_identifier(self) -> builtins.str:
        '''The GatewayIdentifier of the Gateway resource.'''
        result = self._values.get("gateway_identifier")
        assert result is not None, "Required property 'gateway_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.GatewayTargetReference",
    jsii_struct_bases=[],
    name_mapping={"gateway_identifier": "gatewayIdentifier", "target_id": "targetId"},
)
class GatewayTargetReference:
    def __init__(
        self,
        *,
        gateway_identifier: builtins.str,
        target_id: builtins.str,
    ) -> None:
        '''A reference to a GatewayTarget resource.

        :param gateway_identifier: The GatewayIdentifier of the GatewayTarget resource.
        :param target_id: The TargetId of the GatewayTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            gateway_target_reference = bedrockagentcore.GatewayTargetReference(
                gateway_identifier="gatewayIdentifier",
                target_id="targetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b0f80d3aca56f187d6dce631a5608c1969f75cc45ffbb5433808d3f24b64e6)
            check_type(argname="argument gateway_identifier", value=gateway_identifier, expected_type=type_hints["gateway_identifier"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_identifier": gateway_identifier,
            "target_id": target_id,
        }

    @builtins.property
    def gateway_identifier(self) -> builtins.str:
        '''The GatewayIdentifier of the GatewayTarget resource.'''
        result = self._values.get("gateway_identifier")
        assert result is not None, "Required property 'gateway_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''The TargetId of the GatewayTarget resource.'''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IBrowserCustomRef")
class IBrowserCustomRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a BrowserCustom.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> BrowserCustomReference:
        '''(experimental) A reference to a BrowserCustom resource.

        :stability: experimental
        '''
        ...


class _IBrowserCustomRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BrowserCustom.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IBrowserCustomRef"

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> BrowserCustomReference:
        '''(experimental) A reference to a BrowserCustom resource.

        :stability: experimental
        '''
        return typing.cast(BrowserCustomReference, jsii.get(self, "browserCustomRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrowserCustomRef).__jsii_proxy_class__ = lambda : _IBrowserCustomRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.ICodeInterpreterCustomRef")
class ICodeInterpreterCustomRef(
    _constructs_77d1e7e8.IConstruct,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CodeInterpreterCustom.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> CodeInterpreterCustomReference:
        '''(experimental) A reference to a CodeInterpreterCustom resource.

        :stability: experimental
        '''
        ...


class _ICodeInterpreterCustomRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CodeInterpreterCustom.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.ICodeInterpreterCustomRef"

    @builtins.property
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> CodeInterpreterCustomReference:
        '''(experimental) A reference to a CodeInterpreterCustom resource.

        :stability: experimental
        '''
        return typing.cast(CodeInterpreterCustomReference, jsii.get(self, "codeInterpreterCustomRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodeInterpreterCustomRef).__jsii_proxy_class__ = lambda : _ICodeInterpreterCustomRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IGatewayRef")
class IGatewayRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a Gateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> GatewayReference:
        '''(experimental) A reference to a Gateway resource.

        :stability: experimental
        '''
        ...


class _IGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Gateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> GatewayReference:
        '''(experimental) A reference to a Gateway resource.

        :stability: experimental
        '''
        return typing.cast(GatewayReference, jsii.get(self, "gatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayRef).__jsii_proxy_class__ = lambda : _IGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IGatewayTargetRef")
class IGatewayTargetRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a GatewayTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayTargetRef")
    def gateway_target_ref(self) -> GatewayTargetReference:
        '''(experimental) A reference to a GatewayTarget resource.

        :stability: experimental
        '''
        ...


class _IGatewayTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IGatewayTargetRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayTargetRef")
    def gateway_target_ref(self) -> GatewayTargetReference:
        '''(experimental) A reference to a GatewayTarget resource.

        :stability: experimental
        '''
        return typing.cast(GatewayTargetReference, jsii.get(self, "gatewayTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayTargetRef).__jsii_proxy_class__ = lambda : _IGatewayTargetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IMemoryRef")
class IMemoryRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a Memory.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="memoryRef")
    def memory_ref(self) -> "MemoryReference":
        '''(experimental) A reference to a Memory resource.

        :stability: experimental
        '''
        ...


class _IMemoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Memory.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IMemoryRef"

    @builtins.property
    @jsii.member(jsii_name="memoryRef")
    def memory_ref(self) -> "MemoryReference":
        '''(experimental) A reference to a Memory resource.

        :stability: experimental
        '''
        return typing.cast("MemoryReference", jsii.get(self, "memoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMemoryRef).__jsii_proxy_class__ = lambda : _IMemoryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IRuntimeEndpointRef")
class IRuntimeEndpointRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a RuntimeEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> "RuntimeEndpointReference":
        '''(experimental) A reference to a RuntimeEndpoint resource.

        :stability: experimental
        '''
        ...


class _IRuntimeEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RuntimeEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IRuntimeEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> "RuntimeEndpointReference":
        '''(experimental) A reference to a RuntimeEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("RuntimeEndpointReference", jsii.get(self, "runtimeEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuntimeEndpointRef).__jsii_proxy_class__ = lambda : _IRuntimeEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_bedrockagentcore.IRuntimeRef")
class IRuntimeRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a Runtime.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> "RuntimeReference":
        '''(experimental) A reference to a Runtime resource.

        :stability: experimental
        '''
        ...


class _IRuntimeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Runtime.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_bedrockagentcore.IRuntimeRef"

    @builtins.property
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> "RuntimeReference":
        '''(experimental) A reference to a Runtime resource.

        :stability: experimental
        '''
        return typing.cast("RuntimeReference", jsii.get(self, "runtimeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuntimeRef).__jsii_proxy_class__ = lambda : _IRuntimeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.MemoryReference",
    jsii_struct_bases=[],
    name_mapping={"memory_arn": "memoryArn"},
)
class MemoryReference:
    def __init__(self, *, memory_arn: builtins.str) -> None:
        '''A reference to a Memory resource.

        :param memory_arn: The MemoryArn of the Memory resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            memory_reference = bedrockagentcore.MemoryReference(
                memory_arn="memoryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74b3fcbed21b451e3876962b07eac0b89aa927286825f06a266f1378a2f1b0f1)
            check_type(argname="argument memory_arn", value=memory_arn, expected_type=type_hints["memory_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "memory_arn": memory_arn,
        }

    @builtins.property
    def memory_arn(self) -> builtins.str:
        '''The MemoryArn of the Memory resource.'''
        result = self._values.get("memory_arn")
        assert result is not None, "Required property 'memory_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.RuntimeEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"agent_runtime_endpoint_arn": "agentRuntimeEndpointArn"},
)
class RuntimeEndpointReference:
    def __init__(self, *, agent_runtime_endpoint_arn: builtins.str) -> None:
        '''A reference to a RuntimeEndpoint resource.

        :param agent_runtime_endpoint_arn: The AgentRuntimeEndpointArn of the RuntimeEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            runtime_endpoint_reference = bedrockagentcore.RuntimeEndpointReference(
                agent_runtime_endpoint_arn="agentRuntimeEndpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__056e5ef22e335ff5e02bdd57f3e564e80393e99c891cc1890f945dd001ef5b8f)
            check_type(argname="argument agent_runtime_endpoint_arn", value=agent_runtime_endpoint_arn, expected_type=type_hints["agent_runtime_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_endpoint_arn": agent_runtime_endpoint_arn,
        }

    @builtins.property
    def agent_runtime_endpoint_arn(self) -> builtins.str:
        '''The AgentRuntimeEndpointArn of the RuntimeEndpoint resource.'''
        result = self._values.get("agent_runtime_endpoint_arn")
        assert result is not None, "Required property 'agent_runtime_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuntimeEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.RuntimeReference",
    jsii_struct_bases=[],
    name_mapping={"agent_runtime_id": "agentRuntimeId"},
)
class RuntimeReference:
    def __init__(self, *, agent_runtime_id: builtins.str) -> None:
        '''A reference to a Runtime resource.

        :param agent_runtime_id: The AgentRuntimeId of the Runtime resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            runtime_reference = bedrockagentcore.RuntimeReference(
                agent_runtime_id="agentRuntimeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8847701d5ac2ffc328a04478df4877176577ccf780cdf31ccc35b7d9bbcc331a)
            check_type(argname="argument agent_runtime_id", value=agent_runtime_id, expected_type=type_hints["agent_runtime_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_id": agent_runtime_id,
        }

    @builtins.property
    def agent_runtime_id(self) -> builtins.str:
        '''The AgentRuntimeId of the Runtime resource.'''
        result = self._values.get("agent_runtime_id")
        assert result is not None, "Required property 'agent_runtime_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuntimeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, IBrowserCustomRef, _ITaggableV2_4e6798f8)
class CfnBrowserCustom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom",
):
    '''AgentCore Browser tool provides a fast, secure, cloud-based browser runtime to enable AI agents to interact with websites at scale.

    For more information about using the custom browser, see `Interact with web applications using Amazon Bedrock AgentCore Browser <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html
    :cloudformationResource: AWS::BedrockAgentCore::BrowserCustom
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_browser_custom = bedrockagentcore.CfnBrowserCustom(self, "MyCfnBrowserCustom",
            name="name",
            network_configuration=bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                network_mode="networkMode",
        
                # the properties below are optional
                vpc_config=bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            ),
        
            # the properties below are optional
            description="description",
            execution_role_arn="executionRoleArn",
            recording_config=bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                enabled=False,
                s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix"
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.BrowserNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the custom browser.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param description: The custom browser.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param recording_config: THe custom browser configuration.
        :param tags: The tags for the custom browser.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e817ad5ee6496ab54cf569758c4d73da62a4d6f5cf0c34866960f6e4677343e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBrowserCustomProps(
            name=name,
            network_configuration=network_configuration,
            description=description,
            execution_role_arn=execution_role_arn,
            recording_config=recording_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromBrowserId")
    @builtins.classmethod
    def from_browser_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        browser_id: builtins.str,
    ) -> IBrowserCustomRef:
        '''Creates a new IBrowserCustomRef from a browserId.

        :param scope: -
        :param id: -
        :param browser_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5d38dc7619d36a2a4f39c13ec237b55f560a41ac9a162b787880e8e6ba2f47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument browser_id", value=browser_id, expected_type=type_hints["browser_id"])
        return typing.cast(IBrowserCustomRef, jsii.sinvoke(cls, "fromBrowserId", [scope, id, browser_id]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12637c5685b21eb50c5acd05eb9308d8266fc2816549a6a2816d9399823e8551)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14f4b2516dbe32242e98828488dc4abcc900e39ac20507ae2fd0d16a3a0457c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserArn")
    def attr_browser_arn(self) -> builtins.str:
        '''The ARN for the custom browser.

        :cloudformationAttribute: BrowserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserId")
    def attr_browser_id(self) -> builtins.str:
        '''The ID for the custom browser.

        :cloudformationAttribute: BrowserId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the custom browser was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the browser creation or operation failed.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the custom browser was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the custom browser.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> BrowserCustomReference:
        '''A reference to a BrowserCustom resource.'''
        return typing.cast(BrowserCustomReference, jsii.get(self, "browserCustomRef"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the custom browser.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c7dc0414899a74bed53146d246f036f214f82b031723849419726e12bcee67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.BrowserNetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89dfccc35ccd0a377234eb3e008038ad66200df7a4f3c63bf61ebf273a7f42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom browser.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16faa304c4f18b8bba1ee70b209c47d9944346a1e88926b4ee4ea5fe723fd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd292342e1165d23c8ce68a72d30c745d42a2586b394e8bcb4aa1ec13e9cc74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordingConfig")
    def recording_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]]:
        '''THe custom browser configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]], jsii.get(self, "recordingConfig"))

    @recording_config.setter
    def recording_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.RecordingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089c5a25d69d7c7abf4193f45206b584472351088cbe92835bb014923a48f2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the custom browser.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e813ff9c64c23f175682396c7a13b02b9193809d3629b73f2ecac10192c8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode", "vpc_config": "vpcConfig"},
    )
    class BrowserNetworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_mode: builtins.str,
            vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The network configuration.

            :param network_mode: The network mode.
            :param vpc_config: Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                browser_network_configuration_property = bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                    network_mode="networkMode",
                
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0d5bebf1ad5159cc9014318eaa4c540145c82225bd9e29170035b0a29d0ee07)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
                check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''The network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.VpcConfigProperty"]]:
            '''Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrowserNetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "s3_location": "s3Location"},
    )
    class RecordingConfigProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBrowserCustom.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The recording configuration.

            :param enabled: The recording configuration for a browser. This structure defines how browser sessions are recorded. Default: - false
            :param s3_location: The S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                recording_config_property = bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                    enabled=False,
                    s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__754929ea2dabad59807821380b38b3ef1b1955a5473f5469b18a7dcc81600948)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The recording configuration for a browser.

            This structure defines how browser sessions are recorded.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html#cfn-bedrockagentcore-browsercustom-recordingconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.S3LocationProperty"]]:
            '''The S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html#cfn-bedrockagentcore-browsercustom-recordingconfig-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBrowserCustom.S3LocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "prefix": "prefix"},
    )
    class S3LocationProperty:
        def __init__(self, *, bucket: builtins.str, prefix: builtins.str) -> None:
            '''The S3 location.

            :param bucket: The S3 location bucket name.
            :param prefix: The S3 location object prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                s3_location_property = bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6787b09f9e077c274ab79cdf45ea5157eec8aea8960e77f8e128fab67b3cbc26)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "prefix": prefix,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The S3 location bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html#cfn-bedrockagentcore-browsercustom-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''The S3 location object prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html#cfn-bedrockagentcore-browsercustom-s3location-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Network mode configuration for VPC.

            :param security_groups: Security groups for VPC.
            :param subnets: Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                vpc_config_property = bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46efbe5ee20e23cd9dc9ee29c1cd041e741b8a0aeb2c0ea76ed3cb6cab180dad)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''Security groups for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html#cfn-bedrockagentcore-browsercustom-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html#cfn-bedrockagentcore-browsercustom-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, ICodeInterpreterCustomRef, _ITaggableV2_4e6798f8)
class CfnCodeInterpreterCustom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom",
):
    '''The AgentCore Code Interpreter tool enables agents to securely execute code in isolated sandbox environments.

    It offers advanced configuration support and seamless integration with popular frameworks.

    For more information about using the custom code interpreter, see `Execute code and analyze data using Amazon Bedrock AgentCore Code Interpreter <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html
    :cloudformationResource: AWS::BedrockAgentCore::CodeInterpreterCustom
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_code_interpreter_custom = bedrockagentcore.CfnCodeInterpreterCustom(self, "MyCfnCodeInterpreterCustom",
            name="name",
            network_configuration=bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                network_mode="networkMode",
        
                # the properties below are optional
                vpc_config=bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            ),
        
            # the properties below are optional
            description="description",
            execution_role_arn="executionRoleArn",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the code interpreter.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param description: The code interpreter description.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param tags: The tags for the code interpreter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aaa167a6af98d626969b5bd2de9377658de4e8d04df0b48dc5916f9e503a029)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCodeInterpreterCustomProps(
            name=name,
            network_configuration=network_configuration,
            description=description,
            execution_role_arn=execution_role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromCodeInterpreterId")
    @builtins.classmethod
    def from_code_interpreter_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        code_interpreter_id: builtins.str,
    ) -> ICodeInterpreterCustomRef:
        '''Creates a new ICodeInterpreterCustomRef from a codeInterpreterId.

        :param scope: -
        :param id: -
        :param code_interpreter_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e6193c6a8378455a4decc0c525a09a78674fd7ad426e58017e57035bc1789a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument code_interpreter_id", value=code_interpreter_id, expected_type=type_hints["code_interpreter_id"])
        return typing.cast(ICodeInterpreterCustomRef, jsii.sinvoke(cls, "fromCodeInterpreterId", [scope, id, code_interpreter_id]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab4b7a28e87b1af264773dfddc0e9da46bb99c921aa85fb942fcc7ca03680597)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6d68ae9ee508df2d25ca9f4fa9a800c1215c05ac37929135ce20e393a44113)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeInterpreterArn")
    def attr_code_interpreter_arn(self) -> builtins.str:
        '''The code interpreter Amazon Resource Name (ARN).

        :cloudformationAttribute: CodeInterpreterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeInterpreterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeInterpreterId")
    def attr_code_interpreter_id(self) -> builtins.str:
        '''The ID of the code interpreter.

        :cloudformationAttribute: CodeInterpreterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeInterpreterId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the code interpreter was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the code interpreter creation or operation failed.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the code interpreter was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the custom code interpreter.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> CodeInterpreterCustomReference:
        '''A reference to a CodeInterpreterCustom resource.'''
        return typing.cast(CodeInterpreterCustomReference, jsii.get(self, "codeInterpreterCustomRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the code interpreter.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58fa8bcb0ec87d3b6f75396018d3eeff06205adbf6ade289f0ac1710d71c909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36911cef74e5cac559eb0b558b639739fba4dccbbc8a224553a0f0a0cace3cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The code interpreter description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33607ff407017e2c7ecefbc727c6f7660550a46fe6b356799810d75ccf8d662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597443cc8b5cdaed2db807a1545702d23f8f925435f13cd3d17111236aba2428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the code interpreter.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466065bbc5e5f3997568d60c567b51bbc4a9a4900e6ce6da9f9499f85329a3a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode", "vpc_config": "vpcConfig"},
    )
    class CodeInterpreterNetworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_mode: builtins.str,
            vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCodeInterpreterCustom.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The network configuration.

            :param network_mode: The network mode.
            :param vpc_config: Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                code_interpreter_network_configuration_property = bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                    network_mode="networkMode",
                
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eae1295735d5d0996afa02b88ef9dddbd193fc77b25f7b69433fd57c1240bb3a)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
                check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''The network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.VpcConfigProperty"]]:
            '''Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCodeInterpreterCustom.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeInterpreterNetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Network mode configuration for VPC.

            :param security_groups: Security groups for VPC.
            :param subnets: Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                vpc_config_property = bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__97c8e6007d5911afbd85662033d4936d1846dbfdc6caa2fb2e69de26653ccc32)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''Security groups for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IGatewayRef, _ITaggableV2_4e6798f8)
class CfnGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway",
):
    '''Amazon Bedrock AgentCore Gateway provides a unified connectivity layer between agents and the tools and resources they need to interact with.

    For more information about creating a gateway, see `Set up an Amazon Bedrock AgentCore gateway <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html
    :cloudformationResource: AWS::BedrockAgentCore::Gateway
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_gateway = bedrockagentcore.CfnGateway(self, "MyCfnGateway",
            authorizer_type="authorizerType",
            name="name",
            protocol_type="protocolType",
            role_arn="roleArn",
        
            # the properties below are optional
            authorizer_configuration=bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
        
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"]
                )
            ),
            description="description",
            exception_level="exceptionLevel",
            kms_key_arn="kmsKeyArn",
            protocol_configuration=bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty(
                mcp=bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                    instructions="instructions",
                    search_type="searchType",
                    supported_versions=["supportedVersions"]
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorizer_type: builtins.str,
        name: builtins.str,
        protocol_type: builtins.str,
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        exception_level: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        protocol_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GatewayProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authorizer_type: The authorizer type for the gateway.
        :param name: The name for the gateway.
        :param protocol_type: The protocol type for the gateway target.
        :param role_arn: 
        :param authorizer_configuration: 
        :param description: The description for the gateway.
        :param exception_level: The exception level for the gateway.
        :param kms_key_arn: The KMS key ARN for the gateway.
        :param protocol_configuration: The protocol configuration for the gateway target.
        :param tags: The tags for the gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__718d4d7128ca57b0228b268f1204c5574e63e51d4e7701a53fd67a1e8ec17c63)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayProps(
            authorizer_type=authorizer_type,
            name=name,
            protocol_type=protocol_type,
            role_arn=role_arn,
            authorizer_configuration=authorizer_configuration,
            description=description,
            exception_level=exception_level,
            kms_key_arn=kms_key_arn,
            protocol_configuration=protocol_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1253940d92e3f35d08808461458766f65528b0878c674311aabd74aa0a76ce30)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e1eb8798612291b5b13aae1ac0d9cb4513c21df38593628be4d5e2fe660886)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time at which the gateway was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayArn")
    def attr_gateway_arn(self) -> builtins.str:
        '''The ARN for the gateway.

        :cloudformationAttribute: GatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayIdentifier")
    def attr_gateway_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayUrl")
    def attr_gateway_url(self) -> builtins.str:
        '''The gateway URL for the gateway.

        :cloudformationAttribute: GatewayUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status for the gateway.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReasons")
    def attr_status_reasons(self) -> typing.List[builtins.str]:
        '''The status reasons for the gateway.

        :cloudformationAttribute: StatusReasons
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStatusReasons"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkloadIdentityDetails")
    def attr_workload_identity_details(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: WorkloadIdentityDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkloadIdentityDetails"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> GatewayReference:
        '''A reference to a Gateway resource.'''
        return typing.cast(GatewayReference, jsii.get(self, "gatewayRef"))

    @builtins.property
    @jsii.member(jsii_name="authorizerType")
    def authorizer_type(self) -> builtins.str:
        '''The authorizer type for the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "authorizerType"))

    @authorizer_type.setter
    def authorizer_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3733b65f293d2d9f1304c9c6a4cfd4c4aa4a9dca54f65a221b403a9fa85809d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faac8d45eefa612f06e0139bc26af7005d13df5a552a63d10084bfbc444fd266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolType")
    def protocol_type(self) -> builtins.str:
        '''The protocol type for the gateway target.'''
        return typing.cast(builtins.str, jsii.get(self, "protocolType"))

    @protocol_type.setter
    def protocol_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2ccf9c2c13ca5a79d82fee59155dfbaa87d3d17ccc1f27959c635732127d90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a750b424a29fb58f4f0dcc52028237d740f0b0b92d8420600048da5b20537f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizerConfiguration")
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.AuthorizerConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.AuthorizerConfigurationProperty"]], jsii.get(self, "authorizerConfiguration"))

    @authorizer_configuration.setter
    def authorizer_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.AuthorizerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c34ffb86639149c1c6323ad6aa1ec7b9f7d9e7f17a5f5306e5d67d30110ba83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89e3b58faac93b47a86d253bd377ccfed6b64d0088167686a5ce5a6f01bc27b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="exceptionLevel")
    def exception_level(self) -> typing.Optional[builtins.str]:
        '''The exception level for the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exceptionLevel"))

    @exception_level.setter
    def exception_level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__791936566b3e629fd378dc6a46c31b1a5134acc616fbd9ed9eebc092ed3be3e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exceptionLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The KMS key ARN for the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d2d9d8c84164d38a9976889d155298546ea61a787e120117719ee748ac6cf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolConfiguration")
    def protocol_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayProtocolConfigurationProperty"]]:
        '''The protocol configuration for the gateway target.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayProtocolConfigurationProperty"]], jsii.get(self, "protocolConfiguration"))

    @protocol_configuration.setter
    def protocol_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayProtocolConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05982d11a516cc3cf2e986a22173b4993c5267490c660a8f123f9c141f3f117b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the gateway.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8136c8abfebcb699dd26d8e65dbb8e7a922f1cdc2f58375541b3436f139609a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_jwt_authorizer": "customJwtAuthorizer"},
    )
    class AuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            custom_jwt_authorizer: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.CustomJWTAuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param custom_jwt_authorizer: The authorizer configuration for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizer_configuration_property = bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
                
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__788309d24193b18115a31defebe9337a71550513b7163a4a603f72832a42ab79)
                check_type(argname="argument custom_jwt_authorizer", value=custom_jwt_authorizer, expected_type=type_hints["custom_jwt_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_jwt_authorizer": custom_jwt_authorizer,
            }

        @builtins.property
        def custom_jwt_authorizer(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGateway.CustomJWTAuthorizerConfigurationProperty"]:
            '''The authorizer configuration for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizerconfiguration.html#cfn-bedrockagentcore-gateway-authorizerconfiguration-customjwtauthorizer
            '''
            result = self._values.get("custom_jwt_authorizer")
            assert result is not None, "Required property 'custom_jwt_authorizer' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGateway.CustomJWTAuthorizerConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_url": "discoveryUrl",
            "allowed_audience": "allowedAudience",
            "allowed_clients": "allowedClients",
        },
    )
    class CustomJWTAuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            discovery_url: builtins.str,
            allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param discovery_url: The discovery URL for the authorizer configuration.
            :param allowed_audience: The allowed audience authorized for the gateway target.
            :param allowed_clients: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_jWTAuthorizer_configuration_property = bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
                
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8cc4944f630bec36007bb93b09eab3e99763f1bed11457e642c0ab535144159e)
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument allowed_audience", value=allowed_audience, expected_type=type_hints["allowed_audience"])
                check_type(argname="argument allowed_clients", value=allowed_clients, expected_type=type_hints["allowed_clients"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_url": discovery_url,
            }
            if allowed_audience is not None:
                self._values["allowed_audience"] = allowed_audience
            if allowed_clients is not None:
                self._values["allowed_clients"] = allowed_clients

        @builtins.property
        def discovery_url(self) -> builtins.str:
            '''The discovery URL for the authorizer configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-discoveryurl
            '''
            result = self._values.get("discovery_url")
            assert result is not None, "Required property 'discovery_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The allowed audience authorized for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedaudience
            '''
            result = self._values.get("allowed_audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_clients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedclients
            '''
            result = self._values.get("allowed_clients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomJWTAuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"mcp": "mcp"},
    )
    class GatewayProtocolConfigurationProperty:
        def __init__(
            self,
            *,
            mcp: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.MCPGatewayConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The protocol configuration.

            :param mcp: The gateway protocol configuration for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                gateway_protocol_configuration_property = bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty(
                    mcp=bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                        instructions="instructions",
                        search_type="searchType",
                        supported_versions=["supportedVersions"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__381e09b484f23635acaed28352a759fdd9ac853b91ce6a848c9ed3892887eb7c)
                check_type(argname="argument mcp", value=mcp, expected_type=type_hints["mcp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mcp": mcp,
            }

        @builtins.property
        def mcp(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGateway.MCPGatewayConfigurationProperty"]:
            '''The gateway protocol configuration for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration.html#cfn-bedrockagentcore-gateway-gatewayprotocolconfiguration-mcp
            '''
            result = self._values.get("mcp")
            assert result is not None, "Required property 'mcp' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGateway.MCPGatewayConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayProtocolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instructions": "instructions",
            "search_type": "searchType",
            "supported_versions": "supportedVersions",
        },
    )
    class MCPGatewayConfigurationProperty:
        def __init__(
            self,
            *,
            instructions: typing.Optional[builtins.str] = None,
            search_type: typing.Optional[builtins.str] = None,
            supported_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The gateway configuration for MCP.

            :param instructions: 
            :param search_type: The MCP gateway configuration search type.
            :param supported_versions: The supported versions for the MCP configuration for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                m_cPGateway_configuration_property = bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                    instructions="instructions",
                    search_type="searchType",
                    supported_versions=["supportedVersions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__caff723b1f8dc289e3e0d1f554fe16628873911a93ec8c36ed92f59cde7798c4)
                check_type(argname="argument instructions", value=instructions, expected_type=type_hints["instructions"])
                check_type(argname="argument search_type", value=search_type, expected_type=type_hints["search_type"])
                check_type(argname="argument supported_versions", value=supported_versions, expected_type=type_hints["supported_versions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instructions is not None:
                self._values["instructions"] = instructions
            if search_type is not None:
                self._values["search_type"] = search_type
            if supported_versions is not None:
                self._values["supported_versions"] = supported_versions

        @builtins.property
        def instructions(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-instructions
            '''
            result = self._values.get("instructions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def search_type(self) -> typing.Optional[builtins.str]:
            '''The MCP gateway configuration search type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-searchtype
            '''
            result = self._values.get("search_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def supported_versions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The supported versions for the MCP configuration for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-supportedversions
            '''
            result = self._values.get("supported_versions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPGatewayConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.WorkloadIdentityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"workload_identity_arn": "workloadIdentityArn"},
    )
    class WorkloadIdentityDetailsProperty:
        def __init__(self, *, workload_identity_arn: builtins.str) -> None:
            '''The workload identity details for the gateway.

            :param workload_identity_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-workloadidentitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                workload_identity_details_property = bedrockagentcore.CfnGateway.WorkloadIdentityDetailsProperty(
                    workload_identity_arn="workloadIdentityArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e940e88ca017f9ccde7a0419db94aaed6321cc4f2368ad6aa9fe229c8d1d8a3a)
                check_type(argname="argument workload_identity_arn", value=workload_identity_arn, expected_type=type_hints["workload_identity_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workload_identity_arn": workload_identity_arn,
            }

        @builtins.property
        def workload_identity_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-workloadidentitydetails.html#cfn-bedrockagentcore-gateway-workloadidentitydetails-workloadidentityarn
            '''
            result = self._values.get("workload_identity_arn")
            assert result is not None, "Required property 'workload_identity_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkloadIdentityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IGatewayTargetRef)
class CfnGatewayTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget",
):
    '''After creating a gateway, you can add targets, which define the tools that your gateway will host.

    For more information about adding gateway targets, see `Add targets to an existing gateway <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html
    :cloudformationResource: AWS::BedrockAgentCore::GatewayTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
        
        cfn_gateway_target = bedrockagentcore.CfnGatewayTarget(self, "MyCfnGatewayTarget",
            credential_provider_configurations=[bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty(
                credential_provider_type="credentialProviderType",
        
                # the properties below are optional
                credential_provider=bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                    api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                        provider_arn="providerArn",
        
                        # the properties below are optional
                        credential_location="credentialLocation",
                        credential_parameter_name="credentialParameterName",
                        credential_prefix="credentialPrefix"
                    ),
                    oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                        provider_arn="providerArn",
                        scopes=["scopes"],
        
                        # the properties below are optional
                        custom_parameters={
                            "custom_parameters_key": "customParameters"
                        }
                    )
                )
            )],
            name="name",
            target_configuration=bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty(
                mcp=bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                    lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                        lambda_arn="lambdaArn",
                        tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                            inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                description="description",
                                input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
        
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                ),
                                name="name",
        
                                # the properties below are optional
                                output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
        
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                )
                            )],
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    ),
                    open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    ),
                    smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    )
                )
            ),
        
            # the properties below are optional
            description="description",
            gateway_identifier="gatewayIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        credential_provider_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.CredentialProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        target_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        gateway_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param credential_provider_configurations: The OAuth credential provider configuration.
        :param name: The name for the gateway target.
        :param target_configuration: The target configuration for the Smithy model target.
        :param description: The description for the gateway target.
        :param gateway_identifier: The gateway ID for the gateway target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca4172cb2708dfeb7420a18b960df15915d2da8589b9495c034bd700c3bd768)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayTargetProps(
            credential_provider_configurations=credential_provider_configurations,
            name=name,
            target_configuration=target_configuration,
            description=description,
            gateway_identifier=gateway_identifier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__facd54b7bb4cca942a82b0859b83ffbee83d2b5964da7507bd01ce76b51602d7)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f55ddaf00701b9be96b4083ffcf99e108df2b912a7fa6a0930aacc493dc19b3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time at which the gateway target was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayArn")
    def attr_gateway_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status for the gateway target.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReasons")
    def attr_status_reasons(self) -> typing.List[builtins.str]:
        '''The status reasons for the gateway target.

        :cloudformationAttribute: StatusReasons
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStatusReasons"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetId")
    def attr_target_id(self) -> builtins.str:
        '''The target ID for the gateway target.

        :cloudformationAttribute: TargetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The time at which the resource was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="gatewayTargetRef")
    def gateway_target_ref(self) -> GatewayTargetReference:
        '''A reference to a GatewayTarget resource.'''
        return typing.cast(GatewayTargetReference, jsii.get(self, "gatewayTargetRef"))

    @builtins.property
    @jsii.member(jsii_name="credentialProviderConfigurations")
    def credential_provider_configurations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]:
        '''The OAuth credential provider configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]], jsii.get(self, "credentialProviderConfigurations"))

    @credential_provider_configurations.setter
    def credential_provider_configurations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__087a7adedbf9e4e0e6abc10f84df215c78eebc146c64c53668096978e91820bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialProviderConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the gateway target.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4fb979142cd31fef07a02c2a4b5e3d0eb49bf962781821346eac630d16fcc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetConfiguration")
    def target_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.TargetConfigurationProperty"]:
        '''The target configuration for the Smithy model target.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.TargetConfigurationProperty"], jsii.get(self, "targetConfiguration"))

    @target_configuration.setter
    def target_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.TargetConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8d18e620b511ca77468615f894540073998d43a19f84c7bd4555618e80c9a3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88eae40375f8237511c7176b5010bb5247cb77ff6160f37b46d60eac254c2403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gatewayIdentifier")
    def gateway_identifier(self) -> typing.Optional[builtins.str]:
        '''The gateway ID for the gateway target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIdentifier"))

    @gateway_identifier.setter
    def gateway_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4c9f5798e9b6c54f5080d4aef35f1a5d286541a90ad283e95cae82b7a8e7de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayIdentifier", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provider_arn": "providerArn",
            "credential_location": "credentialLocation",
            "credential_parameter_name": "credentialParameterName",
            "credential_prefix": "credentialPrefix",
        },
    )
    class ApiKeyCredentialProviderProperty:
        def __init__(
            self,
            *,
            provider_arn: builtins.str,
            credential_location: typing.Optional[builtins.str] = None,
            credential_parameter_name: typing.Optional[builtins.str] = None,
            credential_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The API key credential provider for the gateway target.

            :param provider_arn: The provider ARN for the gateway target.
            :param credential_location: The credential location for the gateway target.
            :param credential_parameter_name: The credential parameter name for the provider for the gateway target.
            :param credential_prefix: The API key credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_key_credential_provider_property = bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                    provider_arn="providerArn",
                
                    # the properties below are optional
                    credential_location="credentialLocation",
                    credential_parameter_name="credentialParameterName",
                    credential_prefix="credentialPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a33b2b3f3a682c83f92cbd3e15b4552ff1592eb43e06b8e26d9bb1e8f1003ecd)
                check_type(argname="argument provider_arn", value=provider_arn, expected_type=type_hints["provider_arn"])
                check_type(argname="argument credential_location", value=credential_location, expected_type=type_hints["credential_location"])
                check_type(argname="argument credential_parameter_name", value=credential_parameter_name, expected_type=type_hints["credential_parameter_name"])
                check_type(argname="argument credential_prefix", value=credential_prefix, expected_type=type_hints["credential_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "provider_arn": provider_arn,
            }
            if credential_location is not None:
                self._values["credential_location"] = credential_location
            if credential_parameter_name is not None:
                self._values["credential_parameter_name"] = credential_parameter_name
            if credential_prefix is not None:
                self._values["credential_prefix"] = credential_prefix

        @builtins.property
        def provider_arn(self) -> builtins.str:
            '''The provider ARN for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-providerarn
            '''
            result = self._values.get("provider_arn")
            assert result is not None, "Required property 'provider_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def credential_location(self) -> typing.Optional[builtins.str]:
            '''The credential location for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentiallocation
            '''
            result = self._values.get("credential_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credential_parameter_name(self) -> typing.Optional[builtins.str]:
            '''The credential parameter name for the provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialparametername
            '''
            result = self._values.get("credential_parameter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credential_prefix(self) -> typing.Optional[builtins.str]:
            '''The API key credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialprefix
            '''
            result = self._values.get("credential_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiKeyCredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"inline_payload": "inlinePayload", "s3": "s3"},
    )
    class ApiSchemaConfigurationProperty:
        def __init__(
            self,
            *,
            inline_payload: typing.Optional[builtins.str] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.S3ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The API schema configuration for the gateway target.

            :param inline_payload: The inline payload for the gateway.
            :param s3: The API schema configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_schema_configuration_property = bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                    inline_payload="inlinePayload",
                    s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                        bucket_owner_account_id="bucketOwnerAccountId",
                        uri="uri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__309e9dda1e6dfcce4b7777150028f4c6782bdc89a099f0ac87ab71e9967a8277)
                check_type(argname="argument inline_payload", value=inline_payload, expected_type=type_hints["inline_payload"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inline_payload is not None:
                self._values["inline_payload"] = inline_payload
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def inline_payload(self) -> typing.Optional[builtins.str]:
            '''The inline payload for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-inlinepayload
            '''
            result = self._values.get("inline_payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.S3ConfigurationProperty"]]:
            '''The API schema configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.S3ConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiSchemaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credential_provider_type": "credentialProviderType",
            "credential_provider": "credentialProvider",
        },
    )
    class CredentialProviderConfigurationProperty:
        def __init__(
            self,
            *,
            credential_provider_type: builtins.str,
            credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.CredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The credential provider configuration for the gateway target.

            :param credential_provider_type: The credential provider type for the gateway target.
            :param credential_provider: The credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                credential_provider_configuration_property = bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty(
                    credential_provider_type="credentialProviderType",
                
                    # the properties below are optional
                    credential_provider=bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                        api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                            provider_arn="providerArn",
                
                            # the properties below are optional
                            credential_location="credentialLocation",
                            credential_parameter_name="credentialParameterName",
                            credential_prefix="credentialPrefix"
                        ),
                        oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                            provider_arn="providerArn",
                            scopes=["scopes"],
                
                            # the properties below are optional
                            custom_parameters={
                                "custom_parameters_key": "customParameters"
                            }
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__149dd633d64001d8edf5b8db5417ed0fc1bfaecff9240452d6911051ec05238e)
                check_type(argname="argument credential_provider_type", value=credential_provider_type, expected_type=type_hints["credential_provider_type"])
                check_type(argname="argument credential_provider", value=credential_provider, expected_type=type_hints["credential_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "credential_provider_type": credential_provider_type,
            }
            if credential_provider is not None:
                self._values["credential_provider"] = credential_provider

        @builtins.property
        def credential_provider_type(self) -> builtins.str:
            '''The credential provider type for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovidertype
            '''
            result = self._values.get("credential_provider_type")
            assert result is not None, "Required property 'credential_provider_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def credential_provider(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderProperty"]]:
            '''The credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovider
            '''
            result = self._values.get("credential_provider")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.CredentialProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CredentialProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_key_credential_provider": "apiKeyCredentialProvider",
            "oauth_credential_provider": "oauthCredentialProvider",
        },
    )
    class CredentialProviderProperty:
        def __init__(
            self,
            *,
            api_key_credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.ApiKeyCredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            oauth_credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.OAuthCredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param api_key_credential_provider: The API key credential provider.
            :param oauth_credential_provider: The OAuth credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                credential_provider_property = bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                    api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                        provider_arn="providerArn",
                
                        # the properties below are optional
                        credential_location="credentialLocation",
                        credential_parameter_name="credentialParameterName",
                        credential_prefix="credentialPrefix"
                    ),
                    oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                        provider_arn="providerArn",
                        scopes=["scopes"],
                
                        # the properties below are optional
                        custom_parameters={
                            "custom_parameters_key": "customParameters"
                        }
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db13937427760cb24e319f55daf7a1b38d00d0bb009b7b145665b608c53b0f5c)
                check_type(argname="argument api_key_credential_provider", value=api_key_credential_provider, expected_type=type_hints["api_key_credential_provider"])
                check_type(argname="argument oauth_credential_provider", value=oauth_credential_provider, expected_type=type_hints["oauth_credential_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if api_key_credential_provider is not None:
                self._values["api_key_credential_provider"] = api_key_credential_provider
            if oauth_credential_provider is not None:
                self._values["oauth_credential_provider"] = oauth_credential_provider

        @builtins.property
        def api_key_credential_provider(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ApiKeyCredentialProviderProperty"]]:
            '''The API key credential provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html#cfn-bedrockagentcore-gatewaytarget-credentialprovider-apikeycredentialprovider
            '''
            result = self._values.get("api_key_credential_provider")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ApiKeyCredentialProviderProperty"]], result)

        @builtins.property
        def oauth_credential_provider(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.OAuthCredentialProviderProperty"]]:
            '''The OAuth credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html#cfn-bedrockagentcore-gatewaytarget-credentialprovider-oauthcredentialprovider
            '''
            result = self._values.get("oauth_credential_provider")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.OAuthCredentialProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_arn": "lambdaArn", "tool_schema": "toolSchema"},
    )
    class McpLambdaTargetConfigurationProperty:
        def __init__(
            self,
            *,
            lambda_arn: builtins.str,
            tool_schema: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.ToolSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The Lambda target configuration.

            :param lambda_arn: The ARN of the Lambda target configuration.
            :param tool_schema: The tool schema configuration for the gateway target MCP configuration for Lambda.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                mcp_lambda_target_configuration_property = bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                    lambda_arn="lambdaArn",
                    tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                        inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                            description="description",
                            input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                type="type",
                
                                # the properties below are optional
                                description="description",
                                items=schema_definition_property_,
                                properties={
                                    "properties_key": schema_definition_property_
                                },
                                required=["required"]
                            ),
                            name="name",
                
                            # the properties below are optional
                            output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                type="type",
                
                                # the properties below are optional
                                description="description",
                                items=schema_definition_property_,
                                properties={
                                    "properties_key": schema_definition_property_
                                },
                                required=["required"]
                            )
                        )],
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6ba80f262600990b7647765d60a5f51fb86eeeaf8708f22bc73e4794e784785)
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
                check_type(argname="argument tool_schema", value=tool_schema, expected_type=type_hints["tool_schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_arn": lambda_arn,
                "tool_schema": tool_schema,
            }

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''The ARN of the Lambda target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tool_schema(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ToolSchemaProperty"]:
            '''The tool schema configuration for the gateway target MCP configuration for Lambda.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-toolschema
            '''
            result = self._values.get("tool_schema")
            assert result is not None, "Required property 'tool_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ToolSchemaProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpLambdaTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_": "lambda",
            "open_api_schema": "openApiSchema",
            "smithy_model": "smithyModel",
        },
    )
    class McpTargetConfigurationProperty:
        def __init__(
            self,
            *,
            lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.McpLambdaTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            open_api_schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.ApiSchemaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            smithy_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.ApiSchemaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The MCP target configuration for the gateway target.

            :param lambda_: The Lambda MCP configuration for the gateway target.
            :param open_api_schema: The OpenApi schema for the gateway target MCP configuration.
            :param smithy_model: The target configuration for the Smithy model target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                mcp_target_configuration_property = bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                    lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                        lambda_arn="lambdaArn",
                        tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                            inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                description="description",
                                input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
                
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                ),
                                name="name",
                
                                # the properties below are optional
                                output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
                
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                )
                            )],
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    ),
                    open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    ),
                    smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b1d88210caa384ede03a06bee42d13165c8bf4cc4206a236d795c44da216e3c)
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument open_api_schema", value=open_api_schema, expected_type=type_hints["open_api_schema"])
                check_type(argname="argument smithy_model", value=smithy_model, expected_type=type_hints["smithy_model"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if open_api_schema is not None:
                self._values["open_api_schema"] = open_api_schema
            if smithy_model is not None:
                self._values["smithy_model"] = smithy_model

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.McpLambdaTargetConfigurationProperty"]]:
            '''The Lambda MCP configuration for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.McpLambdaTargetConfigurationProperty"]], result)

        @builtins.property
        def open_api_schema(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ApiSchemaConfigurationProperty"]]:
            '''The OpenApi schema for the gateway target MCP configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-openapischema
            '''
            result = self._values.get("open_api_schema")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ApiSchemaConfigurationProperty"]], result)

        @builtins.property
        def smithy_model(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ApiSchemaConfigurationProperty"]]:
            '''The target configuration for the Smithy model target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-smithymodel
            '''
            result = self._values.get("smithy_model")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ApiSchemaConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provider_arn": "providerArn",
            "scopes": "scopes",
            "custom_parameters": "customParameters",
        },
    )
    class OAuthCredentialProviderProperty:
        def __init__(
            self,
            *,
            provider_arn: builtins.str,
            scopes: typing.Sequence[builtins.str],
            custom_parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The OAuth credential provider for the gateway target.

            :param provider_arn: The provider ARN for the gateway target.
            :param scopes: The OAuth credential provider scopes.
            :param custom_parameters: The OAuth credential provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                o_auth_credential_provider_property = bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                    provider_arn="providerArn",
                    scopes=["scopes"],
                
                    # the properties below are optional
                    custom_parameters={
                        "custom_parameters_key": "customParameters"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c602c1e6012421bcbacb23364333a8030b673b0a8e3ebad72fba42b295c2f64)
                check_type(argname="argument provider_arn", value=provider_arn, expected_type=type_hints["provider_arn"])
                check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
                check_type(argname="argument custom_parameters", value=custom_parameters, expected_type=type_hints["custom_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "provider_arn": provider_arn,
                "scopes": scopes,
            }
            if custom_parameters is not None:
                self._values["custom_parameters"] = custom_parameters

        @builtins.property
        def provider_arn(self) -> builtins.str:
            '''The provider ARN for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-providerarn
            '''
            result = self._values.get("provider_arn")
            assert result is not None, "Required property 'provider_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scopes(self) -> typing.List[builtins.str]:
            '''The OAuth credential provider scopes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-scopes
            '''
            result = self._values.get("scopes")
            assert result is not None, "Required property 'scopes' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def custom_parameters(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The OAuth credential provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-customparameters
            '''
            result = self._values.get("custom_parameters")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuthCredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_owner_account_id": "bucketOwnerAccountId", "uri": "uri"},
    )
    class S3ConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_owner_account_id: typing.Optional[builtins.str] = None,
            uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The S3 configuration for the gateway target.

            :param bucket_owner_account_id: The S3 configuration bucket owner account ID for the gateway target.
            :param uri: The configuration URI for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                s3_configuration_property = bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                    bucket_owner_account_id="bucketOwnerAccountId",
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f0b1feb9921a2069b72a9a314cb583fbbc6b6fc8af438b2e8f420e03d0368f7)
                check_type(argname="argument bucket_owner_account_id", value=bucket_owner_account_id, expected_type=type_hints["bucket_owner_account_id"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_owner_account_id is not None:
                self._values["bucket_owner_account_id"] = bucket_owner_account_id
            if uri is not None:
                self._values["uri"] = uri

        @builtins.property
        def bucket_owner_account_id(self) -> typing.Optional[builtins.str]:
            '''The S3 configuration bucket owner account ID for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html#cfn-bedrockagentcore-gatewaytarget-s3configuration-bucketowneraccountid
            '''
            result = self._values.get("bucket_owner_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            '''The configuration URI for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html#cfn-bedrockagentcore-gatewaytarget-s3configuration-uri
            '''
            result = self._values.get("uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "description": "description",
            "items": "items",
            "properties": "properties",
            "required": "required",
        },
    )
    class SchemaDefinitionProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            description: typing.Optional[builtins.str] = None,
            items: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            required: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The schema definition for the gateway target.

            :param type: The scheme definition type for the gateway target.
            :param description: The workload identity details for the gateway.
            :param items: 
            :param properties: The schema definition properties for the gateway target.
            :param required: The schema definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                schema_definition_property = bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                    type="type",
                
                    # the properties below are optional
                    description="description",
                    items=schema_definition_property_,
                    properties={
                        "properties_key": schema_definition_property_
                    },
                    required=["required"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc512741cd348cf43b33e4ea0df31aae8766e6990dc0675d9111d9a7eb5f9c6a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument items", value=items, expected_type=type_hints["items"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if description is not None:
                self._values["description"] = description
            if items is not None:
                self._values["items"] = items
            if properties is not None:
                self._values["properties"] = properties
            if required is not None:
                self._values["required"] = required

        @builtins.property
        def type(self) -> builtins.str:
            '''The scheme definition type for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The workload identity details for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def items(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-items
            '''
            result = self._values.get("items")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]]]]:
            '''The schema definition properties for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]]]], result)

        @builtins.property
        def required(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The schema definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"mcp": "mcp"},
    )
    class TargetConfigurationProperty:
        def __init__(
            self,
            *,
            mcp: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.McpTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The target configuration.

            :param mcp: The target configuration definition for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                target_configuration_property = bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty(
                    mcp=bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                        lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                            lambda_arn="lambdaArn",
                            tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                                inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                    description="description",
                                    input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
                
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    ),
                                    name="name",
                
                                    # the properties below are optional
                                    output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
                
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    )
                                )],
                                s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                    bucket_owner_account_id="bucketOwnerAccountId",
                                    uri="uri"
                                )
                            )
                        ),
                        open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        ),
                        smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a64335e118208df2b03631e56ce84dab935a9d2c9dee1c27c584de679d4dcd6)
                check_type(argname="argument mcp", value=mcp, expected_type=type_hints["mcp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mcp": mcp,
            }

        @builtins.property
        def mcp(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.McpTargetConfigurationProperty"]:
            '''The target configuration definition for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-mcp
            '''
            result = self._values.get("mcp")
            assert result is not None, "Required property 'mcp' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.McpTargetConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "input_schema": "inputSchema",
            "name": "name",
            "output_schema": "outputSchema",
        },
    )
    class ToolDefinitionProperty:
        def __init__(
            self,
            *,
            description: builtins.str,
            input_schema: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            output_schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The tool definition for the gateway.

            :param description: 
            :param input_schema: The input schema for the gateway target.
            :param name: The tool name.
            :param output_schema: The tool definition output schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                tool_definition_property = bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                    description="description",
                    input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                        type="type",
                
                        # the properties below are optional
                        description="description",
                        items=schema_definition_property_,
                        properties={
                            "properties_key": schema_definition_property_
                        },
                        required=["required"]
                    ),
                    name="name",
                
                    # the properties below are optional
                    output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                        type="type",
                
                        # the properties below are optional
                        description="description",
                        items=schema_definition_property_,
                        properties={
                            "properties_key": schema_definition_property_
                        },
                        required=["required"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c9a8204fd6db934022c917c4dc62346cf5269b544292d1bac5ed2aae995a300)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument output_schema", value=output_schema, expected_type=type_hints["output_schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "description": description,
                "input_schema": input_schema,
                "name": name,
            }
            if output_schema is not None:
                self._values["output_schema"] = output_schema

        @builtins.property
        def description(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-description
            '''
            result = self._values.get("description")
            assert result is not None, "Required property 'description' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_schema(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]:
            '''The input schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-inputschema
            '''
            result = self._values.get("input_schema")
            assert result is not None, "Required property 'input_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The tool name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_schema(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]]:
            '''The tool definition output schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-outputschema
            '''
            result = self._values.get("output_schema")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.SchemaDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ToolDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"inline_payload": "inlinePayload", "s3": "s3"},
    )
    class ToolSchemaProperty:
        def __init__(
            self,
            *,
            inline_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.ToolDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGatewayTarget.S3ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The tool schema for the gateway target.

            :param inline_payload: The inline payload for the gateway target.
            :param s3: The S3 tool schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                tool_schema_property = bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                    inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                        description="description",
                        input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                            type="type",
                
                            # the properties below are optional
                            description="description",
                            items=schema_definition_property_,
                            properties={
                                "properties_key": schema_definition_property_
                            },
                            required=["required"]
                        ),
                        name="name",
                
                        # the properties below are optional
                        output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                            type="type",
                
                            # the properties below are optional
                            description="description",
                            items=schema_definition_property_,
                            properties={
                                "properties_key": schema_definition_property_
                            },
                            required=["required"]
                        )
                    )],
                    s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                        bucket_owner_account_id="bucketOwnerAccountId",
                        uri="uri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ff8fed96fdad56eb717513408b41cd94cf1c34461313bbb4de520c38aeab416)
                check_type(argname="argument inline_payload", value=inline_payload, expected_type=type_hints["inline_payload"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inline_payload is not None:
                self._values["inline_payload"] = inline_payload
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def inline_payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ToolDefinitionProperty"]]]]:
            '''The inline payload for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html#cfn-bedrockagentcore-gatewaytarget-toolschema-inlinepayload
            '''
            result = self._values.get("inline_payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.ToolDefinitionProperty"]]]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.S3ConfigurationProperty"]]:
            '''The S3 tool schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html#cfn-bedrockagentcore-gatewaytarget-toolschema-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGatewayTarget.S3ConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ToolSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IMemoryRef, _ITaggableV2_4e6798f8)
class CfnMemory(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory",
):
    '''Memory allows AI agents to maintain both immediate and long-term knowledge, enabling context-aware and personalized interactions.

    For more information about using Memory in Amazon Bedrock AgentCore, see `Host agent or tools with Amazon Bedrock AgentCore Memory <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-getting-started.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html
    :cloudformationResource: AWS::BedrockAgentCore::Memory
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_memory = bedrockagentcore.CfnMemory(self, "MyCfnMemory",
            event_expiry_duration=123,
            name="name",
        
            # the properties below are optional
            description="description",
            encryption_key_arn="encryptionKeyArn",
            memory_execution_role_arn="memoryExecutionRoleArn",
            memory_strategies=[bedrockagentcore.CfnMemory.MemoryStrategyProperty(
                custom_memory_strategy=bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                        self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                            historical_context_window_size=123,
                            invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                payload_delivery_bucket_name="payloadDeliveryBucketName",
                                topic_arn="topicArn"
                            ),
                            trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                    message_count=123
                                ),
                                time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                    idle_session_timeout=123
                                ),
                                token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                    token_count=123
                                )
                            )]
                        ),
                        semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        )
                    ),
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                semantic_memory_strategy=bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                summary_memory_strategy=bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                user_preference_memory_strategy=bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            )],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        event_expiry_duration: jsii.Number,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        memory_execution_role_arn: typing.Optional[builtins.str] = None,
        memory_strategies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.MemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_expiry_duration: The event expiry configuration.
        :param name: The memory name.
        :param description: Description of the Memory resource.
        :param encryption_key_arn: The memory encryption key Amazon Resource Name (ARN).
        :param memory_execution_role_arn: The memory role ARN.
        :param memory_strategies: The memory strategies.
        :param tags: The tags for the resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b95a7255db9df73ca225a32aecd624481667f18f3308ba77ce3fbf7d7e1cf4f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMemoryProps(
            event_expiry_duration=event_expiry_duration,
            name=name,
            description=description,
            encryption_key_arn=encryption_key_arn,
            memory_execution_role_arn=memory_execution_role_arn,
            memory_strategies=memory_strategies,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b76cbb12d67c915a322289eef0caf05911a64361531f525f945065e6fbd1b0b)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29efd6b6b9a6ac1e7281cd85ae63e9d6002789f18830f68a7cec0a0d012ac382)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the memory record was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''
        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrMemoryArn")
    def attr_memory_arn(self) -> builtins.str:
        '''ARN of the Memory resource.

        :cloudformationAttribute: MemoryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMemoryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMemoryId")
    def attr_memory_id(self) -> builtins.str:
        '''The memory ID.

        :cloudformationAttribute: MemoryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMemoryId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The memory status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="memoryRef")
    def memory_ref(self) -> MemoryReference:
        '''A reference to a Memory resource.'''
        return typing.cast(MemoryReference, jsii.get(self, "memoryRef"))

    @builtins.property
    @jsii.member(jsii_name="eventExpiryDuration")
    def event_expiry_duration(self) -> jsii.Number:
        '''The event expiry configuration.'''
        return typing.cast(jsii.Number, jsii.get(self, "eventExpiryDuration"))

    @event_expiry_duration.setter
    def event_expiry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c376bc3bd26c18cf626509568f040ac75ef52a68ef8a39ca3e5b6b8308374496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventExpiryDuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The memory name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f948061bc9aba0eb248f047c217bd96c19cf47d09da3c7b9708380caf387394f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the Memory resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93e29c7f80206ddbc4de97f028b669d82daf8dd5c65b29ae535035b57cd461ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The memory encryption key Amazon Resource Name (ARN).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b682a270f87cf6f76b16e70568b3e20c1994f4ff375efed9e59f3ff29cce80cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memoryExecutionRoleArn")
    def memory_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The memory role ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryExecutionRoleArn"))

    @memory_execution_role_arn.setter
    def memory_execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bd6b17fbf9c4464799eba94f4be79124e7c5491b62da83c1a8bd39d6f2a0def)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryExecutionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memoryStrategies")
    def memory_strategies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.MemoryStrategyProperty"]]]]:
        '''The memory strategies.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.MemoryStrategyProperty"]]]], jsii.get(self, "memoryStrategies"))

    @memory_strategies.setter
    def memory_strategies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.MemoryStrategyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b18515e6738d6694af7855ee5a84c8940fcfa482c5e51f03ea9e0abda4a56765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryStrategies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the resources.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20937c3b9ee32cb1df4d7eaf09c5da2b921076b8dab073c8f61380cb9b64e33b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.CustomConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "self_managed_configuration": "selfManagedConfiguration",
            "semantic_override": "semanticOverride",
            "summary_override": "summaryOverride",
            "user_preference_override": "userPreferenceOverride",
        },
    )
    class CustomConfigurationInputProperty:
        def __init__(
            self,
            *,
            self_managed_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SelfManagedConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            semantic_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SemanticOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            summary_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SummaryOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_preference_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.UserPreferenceOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory configuration input.

            :param self_managed_configuration: The custom configuration input.
            :param semantic_override: The memory override configuration.
            :param summary_override: The memory configuration override.
            :param user_preference_override: The memory user preference override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_configuration_input_property = bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                    self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                        historical_context_window_size=123,
                        invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                            payload_delivery_bucket_name="payloadDeliveryBucketName",
                            topic_arn="topicArn"
                        ),
                        trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                            message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                message_count=123
                            ),
                            time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                idle_session_timeout=123
                            ),
                            token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                token_count=123
                            )
                        )]
                    ),
                    semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        ),
                        extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        )
                    ),
                    summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        )
                    ),
                    user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        ),
                        extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80b393ad440afaf6b639d0ad3fdd1431e23bc8fa4658d92c51bbe3ae892ec72e)
                check_type(argname="argument self_managed_configuration", value=self_managed_configuration, expected_type=type_hints["self_managed_configuration"])
                check_type(argname="argument semantic_override", value=semantic_override, expected_type=type_hints["semantic_override"])
                check_type(argname="argument summary_override", value=summary_override, expected_type=type_hints["summary_override"])
                check_type(argname="argument user_preference_override", value=user_preference_override, expected_type=type_hints["user_preference_override"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if self_managed_configuration is not None:
                self._values["self_managed_configuration"] = self_managed_configuration
            if semantic_override is not None:
                self._values["semantic_override"] = semantic_override
            if summary_override is not None:
                self._values["summary_override"] = summary_override
            if user_preference_override is not None:
                self._values["user_preference_override"] = user_preference_override

        @builtins.property
        def self_managed_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SelfManagedConfigurationProperty"]]:
            '''The custom configuration input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-selfmanagedconfiguration
            '''
            result = self._values.get("self_managed_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SelfManagedConfigurationProperty"]], result)

        @builtins.property
        def semantic_override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticOverrideProperty"]]:
            '''The memory override configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-semanticoverride
            '''
            result = self._values.get("semantic_override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticOverrideProperty"]], result)

        @builtins.property
        def summary_override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SummaryOverrideProperty"]]:
            '''The memory configuration override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-summaryoverride
            '''
            result = self._values.get("summary_override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SummaryOverrideProperty"]], result)

        @builtins.property
        def user_preference_override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceOverrideProperty"]]:
            '''The memory user preference override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-userpreferenceoverride
            '''
            result = self._values.get("user_preference_override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceOverrideProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "configuration": "configuration",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class CustomMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.CustomConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param configuration: The memory strategy configuration.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The memory strategy namespaces.
            :param status: The memory strategy status.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_memory_strategy_property = bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                        self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                            historical_context_window_size=123,
                            invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                payload_delivery_bucket_name="payloadDeliveryBucketName",
                                topic_arn="topicArn"
                            ),
                            trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                    message_count=123
                                ),
                                time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                    idle_session_timeout=123
                                ),
                                token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                    token_count=123
                                )
                            )]
                        ),
                        semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        )
                    ),
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68f9ef2809f813258bef3dcd9ec460d2f237f2127d9f7cb9aae3256166ba8183)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if configuration is not None:
                self._values["configuration"] = configuration
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.CustomConfigurationInputProperty"]]:
            '''The memory strategy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-configuration
            '''
            result = self._values.get("configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.CustomConfigurationInputProperty"]], result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The memory strategy namespaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The memory strategy status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "payload_delivery_bucket_name": "payloadDeliveryBucketName",
            "topic_arn": "topicArn",
        },
    )
    class InvocationConfigurationInputProperty:
        def __init__(
            self,
            *,
            payload_delivery_bucket_name: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory invocation configuration input.

            :param payload_delivery_bucket_name: The message invocation configuration information for the bucket name.
            :param topic_arn: The memory trigger condition topic Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                invocation_configuration_input_property = bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                    payload_delivery_bucket_name="payloadDeliveryBucketName",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44e7fa751a69795001dc84cc0fd23b36ae6952ce8c475d549b7599b3353a7c9a)
                check_type(argname="argument payload_delivery_bucket_name", value=payload_delivery_bucket_name, expected_type=type_hints["payload_delivery_bucket_name"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if payload_delivery_bucket_name is not None:
                self._values["payload_delivery_bucket_name"] = payload_delivery_bucket_name
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def payload_delivery_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The message invocation configuration information for the bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html#cfn-bedrockagentcore-memory-invocationconfigurationinput-payloaddeliverybucketname
            '''
            result = self._values.get("payload_delivery_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The memory trigger condition topic Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html#cfn-bedrockagentcore-memory-invocationconfigurationinput-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InvocationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.MemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_memory_strategy": "customMemoryStrategy",
            "semantic_memory_strategy": "semanticMemoryStrategy",
            "summary_memory_strategy": "summaryMemoryStrategy",
            "user_preference_memory_strategy": "userPreferenceMemoryStrategy",
        },
    )
    class MemoryStrategyProperty:
        def __init__(
            self,
            *,
            custom_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.CustomMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            semantic_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SemanticMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            summary_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SummaryMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_preference_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.UserPreferenceMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory strategy.

            :param custom_memory_strategy: The memory strategy.
            :param semantic_memory_strategy: The memory strategy.
            :param summary_memory_strategy: The memory strategy summary.
            :param user_preference_memory_strategy: The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                memory_strategy_property = bedrockagentcore.CfnMemory.MemoryStrategyProperty(
                    custom_memory_strategy=bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                            self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                                historical_context_window_size=123,
                                invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                    payload_delivery_bucket_name="payloadDeliveryBucketName",
                                    topic_arn="topicArn"
                                ),
                                trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                    message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                        message_count=123
                                    ),
                                    time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                        idle_session_timeout=123
                                    ),
                                    token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                        token_count=123
                                    )
                                )]
                            ),
                            semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            )
                        ),
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    semantic_memory_strategy=bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    summary_memory_strategy=bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    user_preference_memory_strategy=bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7fa25b2413ebaf6794a4e0d96d4404f578a37b86cd501369f7c93f8d049e8e7)
                check_type(argname="argument custom_memory_strategy", value=custom_memory_strategy, expected_type=type_hints["custom_memory_strategy"])
                check_type(argname="argument semantic_memory_strategy", value=semantic_memory_strategy, expected_type=type_hints["semantic_memory_strategy"])
                check_type(argname="argument summary_memory_strategy", value=summary_memory_strategy, expected_type=type_hints["summary_memory_strategy"])
                check_type(argname="argument user_preference_memory_strategy", value=user_preference_memory_strategy, expected_type=type_hints["user_preference_memory_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_memory_strategy is not None:
                self._values["custom_memory_strategy"] = custom_memory_strategy
            if semantic_memory_strategy is not None:
                self._values["semantic_memory_strategy"] = semantic_memory_strategy
            if summary_memory_strategy is not None:
                self._values["summary_memory_strategy"] = summary_memory_strategy
            if user_preference_memory_strategy is not None:
                self._values["user_preference_memory_strategy"] = user_preference_memory_strategy

        @builtins.property
        def custom_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.CustomMemoryStrategyProperty"]]:
            '''The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-custommemorystrategy
            '''
            result = self._values.get("custom_memory_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.CustomMemoryStrategyProperty"]], result)

        @builtins.property
        def semantic_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticMemoryStrategyProperty"]]:
            '''The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-semanticmemorystrategy
            '''
            result = self._values.get("semantic_memory_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticMemoryStrategyProperty"]], result)

        @builtins.property
        def summary_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SummaryMemoryStrategyProperty"]]:
            '''The memory strategy summary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-summarymemorystrategy
            '''
            result = self._values.get("summary_memory_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SummaryMemoryStrategyProperty"]], result)

        @builtins.property
        def user_preference_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceMemoryStrategyProperty"]]:
            '''The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-userpreferencememorystrategy
            '''
            result = self._values.get("user_preference_memory_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceMemoryStrategyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty",
        jsii_struct_bases=[],
        name_mapping={"message_count": "messageCount"},
    )
    class MessageBasedTriggerInputProperty:
        def __init__(
            self,
            *,
            message_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The message based trigger input.

            :param message_count: The memory trigger condition input for the message based trigger message count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-messagebasedtriggerinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                message_based_trigger_input_property = bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                    message_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f26f0bfb6bb91a96529926b34610d43ded0571d826aa8ac6cb6e63367e9ea089)
                check_type(argname="argument message_count", value=message_count, expected_type=type_hints["message_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_count is not None:
                self._values["message_count"] = message_count

        @builtins.property
        def message_count(self) -> typing.Optional[jsii.Number]:
            '''The memory trigger condition input for the message based trigger message count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-messagebasedtriggerinput.html#cfn-bedrockagentcore-memory-messagebasedtriggerinput-messagecount
            '''
            result = self._values.get("message_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageBasedTriggerInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "historical_context_window_size": "historicalContextWindowSize",
            "invocation_configuration": "invocationConfiguration",
            "trigger_conditions": "triggerConditions",
        },
    )
    class SelfManagedConfigurationProperty:
        def __init__(
            self,
            *,
            historical_context_window_size: typing.Optional[jsii.Number] = None,
            invocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.InvocationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trigger_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.TriggerConditionInputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The self managed configuration.

            :param historical_context_window_size: The memory configuration for self managed.
            :param invocation_configuration: The self managed configuration.
            :param trigger_conditions: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                self_managed_configuration_property = bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                    historical_context_window_size=123,
                    invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                        payload_delivery_bucket_name="payloadDeliveryBucketName",
                        topic_arn="topicArn"
                    ),
                    trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                        message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                            message_count=123
                        ),
                        time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                            idle_session_timeout=123
                        ),
                        token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                            token_count=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4fcd7b9f7c5c0bb0c80ff54635936b78ada2b3d24596ba7cd43b9ece93f804c)
                check_type(argname="argument historical_context_window_size", value=historical_context_window_size, expected_type=type_hints["historical_context_window_size"])
                check_type(argname="argument invocation_configuration", value=invocation_configuration, expected_type=type_hints["invocation_configuration"])
                check_type(argname="argument trigger_conditions", value=trigger_conditions, expected_type=type_hints["trigger_conditions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if historical_context_window_size is not None:
                self._values["historical_context_window_size"] = historical_context_window_size
            if invocation_configuration is not None:
                self._values["invocation_configuration"] = invocation_configuration
            if trigger_conditions is not None:
                self._values["trigger_conditions"] = trigger_conditions

        @builtins.property
        def historical_context_window_size(self) -> typing.Optional[jsii.Number]:
            '''The memory configuration for self managed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html#cfn-bedrockagentcore-memory-selfmanagedconfiguration-historicalcontextwindowsize
            '''
            result = self._values.get("historical_context_window_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def invocation_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.InvocationConfigurationInputProperty"]]:
            '''The self managed configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html#cfn-bedrockagentcore-memory-selfmanagedconfiguration-invocationconfiguration
            '''
            result = self._values.get("invocation_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.InvocationConfigurationInputProperty"]], result)

        @builtins.property
        def trigger_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.TriggerConditionInputProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html#cfn-bedrockagentcore-memory-selfmanagedconfiguration-triggerconditions
            '''
            result = self._values.get("trigger_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMemory.TriggerConditionInputProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class SemanticMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The memory strategy namespaces.
            :param status: Status of the memory strategy.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: Last update timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_memory_strategy_property = bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fdd1426fa7487dcb02499d9f810acd963031578a3c30fd4be0b076b09a32b124)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The memory strategy namespaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Status of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''Last update timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class SemanticOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The memory override configuration.

            :param append_to_prompt: The override configuration.
            :param model_id: The memory override model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__393b5baf9d5b39c6498ec7dde998e56d10f272578b90e6901d6e5717c4d0b79d)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The override configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class SemanticOverrideExtractionConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The memory override configuration.

            :param append_to_prompt: The extraction configuration.
            :param model_id: The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_override_extraction_configuration_input_property = bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__669cd3ffc171b2cd7f3a4c3d6196e5a075449bedd07119892324a275601cf283)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The extraction configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticOverrideExtractionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"consolidation": "consolidation", "extraction": "extraction"},
    )
    class SemanticOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SemanticOverrideExtractionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory override.

            :param consolidation: The memory override consolidation.
            :param extraction: The memory override extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_override_property = bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    ),
                    extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4fcd9046e68a8e9401f48408f0a4870f5c13f714c342e2085d178557990c4ee)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
                check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation
            if extraction is not None:
                self._values["extraction"] = extraction

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty"]]:
            '''The memory override consolidation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverride.html#cfn-bedrockagentcore-memory-semanticoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty"]], result)

        @builtins.property
        def extraction(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticOverrideExtractionConfigurationInputProperty"]]:
            '''The memory override extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverride.html#cfn-bedrockagentcore-memory-semanticoverride-extraction
            '''
            result = self._values.get("extraction")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SemanticOverrideExtractionConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class SummaryMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The summary memory strategy.
            :param status: The memory strategy status.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                summary_memory_strategy_property = bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eee517e4354bf11f650f3de6c9e3789b5ced3c958c97582b32deda0a2643b376)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The summary memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The memory strategy status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SummaryMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class SummaryOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The consolidation configuration.

            :param append_to_prompt: The memory override configuration.
            :param model_id: The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                summary_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c990b6378d188092fe95d78caab0eb586836dc0ca2194f9cbf3788c24c6ec053)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The memory override configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SummaryOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SummaryOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"consolidation": "consolidation"},
    )
    class SummaryOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory summary override.

            :param consolidation: The memory override consolidation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                summary_override_property = bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b23ed198bcd958ec3a014c4dd2d6c418b82bc1895ca1b0af24503f002e61d492)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty"]]:
            '''The memory override consolidation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverride.html#cfn-bedrockagentcore-memory-summaryoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SummaryOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty",
        jsii_struct_bases=[],
        name_mapping={"idle_session_timeout": "idleSessionTimeout"},
    )
    class TimeBasedTriggerInputProperty:
        def __init__(
            self,
            *,
            idle_session_timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The memory trigger condition input for the time based trigger.

            :param idle_session_timeout: The memory trigger condition input for the session timeout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-timebasedtriggerinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                time_based_trigger_input_property = bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                    idle_session_timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0cf65bf0b7de7a122f8fdf3c50a61ba88dd5248ad841dd004cb6bd0f7174ec45)
                check_type(argname="argument idle_session_timeout", value=idle_session_timeout, expected_type=type_hints["idle_session_timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if idle_session_timeout is not None:
                self._values["idle_session_timeout"] = idle_session_timeout

        @builtins.property
        def idle_session_timeout(self) -> typing.Optional[jsii.Number]:
            '''The memory trigger condition input for the session timeout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-timebasedtriggerinput.html#cfn-bedrockagentcore-memory-timebasedtriggerinput-idlesessiontimeout
            '''
            result = self._values.get("idle_session_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedTriggerInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty",
        jsii_struct_bases=[],
        name_mapping={"token_count": "tokenCount"},
    )
    class TokenBasedTriggerInputProperty:
        def __init__(self, *, token_count: typing.Optional[jsii.Number] = None) -> None:
            '''The token based trigger input.

            :param token_count: The token based trigger token count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                token_based_trigger_input_property = bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                    token_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__171b0765936a13c6e7c17456605ec3e2bc9c36685a864e8c11187bfd9a4bc89a)
                check_type(argname="argument token_count", value=token_count, expected_type=type_hints["token_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if token_count is not None:
                self._values["token_count"] = token_count

        @builtins.property
        def token_count(self) -> typing.Optional[jsii.Number]:
            '''The token based trigger token count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.html#cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount
            '''
            result = self._values.get("token_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TokenBasedTriggerInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.TriggerConditionInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message_based_trigger": "messageBasedTrigger",
            "time_based_trigger": "timeBasedTrigger",
            "token_based_trigger": "tokenBasedTrigger",
        },
    )
    class TriggerConditionInputProperty:
        def __init__(
            self,
            *,
            message_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.MessageBasedTriggerInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            time_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.TimeBasedTriggerInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            token_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.TokenBasedTriggerInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory trigger condition input.

            :param message_based_trigger: The memory trigger condition input for the message based trigger.
            :param time_based_trigger: The memory trigger condition input.
            :param token_based_trigger: The trigger condition information for a token based trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                trigger_condition_input_property = bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                    message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                        message_count=123
                    ),
                    time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                        idle_session_timeout=123
                    ),
                    token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                        token_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9ca3b096b467bf1778a21961da57f12ce16cf0ef63aeee1b912577f66fdb48cb)
                check_type(argname="argument message_based_trigger", value=message_based_trigger, expected_type=type_hints["message_based_trigger"])
                check_type(argname="argument time_based_trigger", value=time_based_trigger, expected_type=type_hints["time_based_trigger"])
                check_type(argname="argument token_based_trigger", value=token_based_trigger, expected_type=type_hints["token_based_trigger"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_based_trigger is not None:
                self._values["message_based_trigger"] = message_based_trigger
            if time_based_trigger is not None:
                self._values["time_based_trigger"] = time_based_trigger
            if token_based_trigger is not None:
                self._values["token_based_trigger"] = token_based_trigger

        @builtins.property
        def message_based_trigger(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.MessageBasedTriggerInputProperty"]]:
            '''The memory trigger condition input for the message based trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html#cfn-bedrockagentcore-memory-triggerconditioninput-messagebasedtrigger
            '''
            result = self._values.get("message_based_trigger")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.MessageBasedTriggerInputProperty"]], result)

        @builtins.property
        def time_based_trigger(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.TimeBasedTriggerInputProperty"]]:
            '''The memory trigger condition input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html#cfn-bedrockagentcore-memory-triggerconditioninput-timebasedtrigger
            '''
            result = self._values.get("time_based_trigger")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.TimeBasedTriggerInputProperty"]], result)

        @builtins.property
        def token_based_trigger(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.TokenBasedTriggerInputProperty"]]:
            '''The trigger condition information for a token based trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html#cfn-bedrockagentcore-memory-triggerconditioninput-tokenbasedtrigger
            '''
            result = self._values.get("token_based_trigger")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.TokenBasedTriggerInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConditionInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class UserPreferenceMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The memory namespaces.
            :param status: The memory strategy status.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_memory_strategy_property = bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__404072c850abd871eb86ee8d04d20a311da6fb4147c983194a800b234cbf1e04)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The memory namespaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The memory strategy status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class UserPreferenceOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The configuration input.

            :param append_to_prompt: The memory configuration.
            :param model_id: The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccf5e9da18deac0b8b6ae4a435ef031fafc5037acda6e9b5a2f31d25335ea0ad)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The memory configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class UserPreferenceOverrideExtractionConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The memory override configuration.

            :param append_to_prompt: The extraction configuration.
            :param model_id: The memory override for the model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_override_extraction_configuration_input_property = bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e2496eed790ccc12ab395eda9327489aa843786babbb42e3d6238d462a4c629)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The extraction configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override for the model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceOverrideExtractionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"consolidation": "consolidation", "extraction": "extraction"},
    )
    class UserPreferenceOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory user preference override.

            :param consolidation: The memory override consolidation information.
            :param extraction: The memory user preferences for extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_override_property = bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    ),
                    extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a657a70bb10847e586abd34f2ecc11ddcafa4b88002f03b52b85d085202adcfd)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
                check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation
            if extraction is not None:
                self._values["extraction"] = extraction

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty"]]:
            '''The memory override consolidation information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html#cfn-bedrockagentcore-memory-userpreferenceoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty"]], result)

        @builtins.property
        def extraction(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty"]]:
            '''The memory user preferences for extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html#cfn-bedrockagentcore-memory-userpreferenceoverride-extraction
            '''
            result = self._values.get("extraction")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IRuntimeRef, _ITaggableV2_4e6798f8)
class CfnRuntime(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime",
):
    '''Contains information about an agent runtime. An agent runtime is the execution environment for a Amazon Bedrock Agent.

    AgentCore Runtime is a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools using any open-source framework including LangGraph, CrewAI, and Strands Agents, any protocol, and any model.

    For more information about using agent runtime in Amazon Bedrock AgentCore, see `Host agent or tools with Amazon Bedrock AgentCore Runtime <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html
    :cloudformationResource: AWS::BedrockAgentCore::Runtime
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_runtime = bedrockagentcore.CfnRuntime(self, "MyCfnRuntime",
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri="containerUri"
                )
            ),
            agent_runtime_name="agentRuntimeName",
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                network_mode="networkMode",
        
                # the properties below are optional
                network_mode_config=bedrockagentcore.CfnRuntime.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
        
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"]
                )
            ),
            description="description",
            environment_variables={
                "environment_variables_key": "environmentVariables"
            },
            protocol_configuration="protocolConfiguration",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AgentRuntimeArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
        agent_runtime_name: builtins.str,
        network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        protocol_configuration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_runtime_artifact: The artifact of the agent.
        :param agent_runtime_name: The name of the AgentCore Runtime endpoint.
        :param network_configuration: The network configuration.
        :param role_arn: The Amazon Resource Name (ARN) for for the role.
        :param authorizer_configuration: Represents inbound authorization configuration options used to authenticate incoming requests.
        :param description: The agent runtime description.
        :param environment_variables: The environment variables for the agent.
        :param protocol_configuration: The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.
        :param tags: The tags for the agent.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f75c2b58380182b53165109480fecdbf9bcd35c2fcfcfea5141466ba05b7e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuntimeProps(
            agent_runtime_artifact=agent_runtime_artifact,
            agent_runtime_name=agent_runtime_name,
            network_configuration=network_configuration,
            role_arn=role_arn,
            authorizer_configuration=authorizer_configuration,
            description=description,
            environment_variables=environment_variables,
            protocol_configuration=protocol_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41eb1aeeb420a432d00eafdf7061763658f434f8c1b3fac5748e0b80cf168cda)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffbc19212156590bcfcec54a917d56095cf1d0e95a1f4f4107501a8cf457feb7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeArn")
    def attr_agent_runtime_arn(self) -> builtins.str:
        '''The agent runtime ARN.

        :cloudformationAttribute: AgentRuntimeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeId")
    def attr_agent_runtime_id(self) -> builtins.str:
        '''The ID for the agent runtime.

        :cloudformationAttribute: AgentRuntimeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeId"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeVersion")
    def attr_agent_runtime_version(self) -> builtins.str:
        '''The version for the agent runtime.

        :cloudformationAttribute: AgentRuntimeVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the runtime was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the runtime was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status for the agent runtime.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkloadIdentityDetails")
    def attr_workload_identity_details(self) -> _IResolvable_da3f097b:
        '''Configuration for workload identity.

        :cloudformationAttribute: WorkloadIdentityDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkloadIdentityDetails"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> RuntimeReference:
        '''A reference to a Runtime resource.'''
        return typing.cast(RuntimeReference, jsii.get(self, "runtimeRef"))

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeArtifact")
    def agent_runtime_artifact(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"]:
        '''The artifact of the agent.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"], jsii.get(self, "agentRuntimeArtifact"))

    @agent_runtime_artifact.setter
    def agent_runtime_artifact(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRuntime.AgentRuntimeArtifactProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afa965e1f7852c99b813a59ddc326e4e8b2e629273fff790e48abcc309421fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeArtifact", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeName")
    def agent_runtime_name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "agentRuntimeName"))

    @agent_runtime_name.setter
    def agent_runtime_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e5f3a5d4d3f3cf24f87565ebb2f7c531ed9e006970eb5a59dee4eeed670f19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"]:
        '''The network configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRuntime.NetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a3b80aa643920bb76e97b49e6d7c54f3367df4203a420045d6d631a4d54658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for for the role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712719ad084eaaa1f88407e6da1dd4ed68fa570a04329676de9d476fde02ebfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizerConfiguration")
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]]:
        '''Represents inbound authorization configuration options used to authenticate incoming requests.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]], jsii.get(self, "authorizerConfiguration"))

    @authorizer_configuration.setter
    def authorizer_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.AuthorizerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577d498b775175712bf02d50d4dc0a7fa74d069187c6c0daba641442a844c29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The agent runtime description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86887c96ad11d54aa9be7288cd5dfe9a9b3cb370236b2cf8c98f0ea09d7246e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''The environment variables for the agent.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b52f571e16cbee3d0cb6aef888169b2fdf172a92199c29075b1bbfe5eb3091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolConfiguration")
    def protocol_configuration(self) -> typing.Optional[builtins.str]:
        '''The protocol configuration for an agent runtime.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolConfiguration"))

    @protocol_configuration.setter
    def protocol_configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd16ca9a4cf1077fb69bea991264277b990667565406b724c960232073239095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the agent.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c0ee18c00618ce3d55cf861e88265d3db540867ff55146671310649d3ccaee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty",
        jsii_struct_bases=[],
        name_mapping={"container_configuration": "containerConfiguration"},
    )
    class AgentRuntimeArtifactProperty:
        def __init__(
            self,
            *,
            container_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.ContainerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The artifact of the agent.

            :param container_configuration: Representation of a container configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                agent_runtime_artifact_property = bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                    container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                        container_uri="containerUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51346444ae527a839c6fcfd4fd456eeea9b11da43bf9dadd9b152cfc716ecfd2)
                check_type(argname="argument container_configuration", value=container_configuration, expected_type=type_hints["container_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_configuration is not None:
                self._values["container_configuration"] = container_configuration

        @builtins.property
        def container_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.ContainerConfigurationProperty"]]:
            '''Representation of a container configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html#cfn-bedrockagentcore-runtime-agentruntimeartifact-containerconfiguration
            '''
            result = self._values.get("container_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.ContainerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentRuntimeArtifactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_jwt_authorizer": "customJwtAuthorizer"},
    )
    class AuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            custom_jwt_authorizer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.CustomJWTAuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The authorizer configuration.

            :param custom_jwt_authorizer: Represents inbound authorization configuration options used to authenticate incoming requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizer_configuration_property = bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
                
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb18338480d08b211086521e0155635de6c3b54cf6ebbb5a7ee690c697991b4b)
                check_type(argname="argument custom_jwt_authorizer", value=custom_jwt_authorizer, expected_type=type_hints["custom_jwt_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_jwt_authorizer is not None:
                self._values["custom_jwt_authorizer"] = custom_jwt_authorizer

        @builtins.property
        def custom_jwt_authorizer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.CustomJWTAuthorizerConfigurationProperty"]]:
            '''Represents inbound authorization configuration options used to authenticate incoming requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizerconfiguration.html#cfn-bedrockagentcore-runtime-authorizerconfiguration-customjwtauthorizer
            '''
            result = self._values.get("custom_jwt_authorizer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.CustomJWTAuthorizerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.ContainerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"container_uri": "containerUri"},
    )
    class ContainerConfigurationProperty:
        def __init__(self, *, container_uri: builtins.str) -> None:
            '''The container configuration.

            :param container_uri: The container Uri.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-containerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                container_configuration_property = bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri="containerUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0740ce1d3425c4e128b2f49784ee2a02ae6e81129ade5290d001575f4ecacb8)
                check_type(argname="argument container_uri", value=container_uri, expected_type=type_hints["container_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_uri": container_uri,
            }

        @builtins.property
        def container_uri(self) -> builtins.str:
            '''The container Uri.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-containerconfiguration.html#cfn-bedrockagentcore-runtime-containerconfiguration-containeruri
            '''
            result = self._values.get("container_uri")
            assert result is not None, "Required property 'container_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_url": "discoveryUrl",
            "allowed_audience": "allowedAudience",
            "allowed_clients": "allowedClients",
        },
    )
    class CustomJWTAuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            discovery_url: builtins.str,
            allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration for custom JWT authorizer.

            :param discovery_url: The configuration authorization.
            :param allowed_audience: Represents inbound authorization configuration options used to authenticate incoming requests.
            :param allowed_clients: Represents individual client IDs that are validated in the incoming JWT token validation process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_jWTAuthorizer_configuration_property = bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
                
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6479ff33c6925aa85dcd6d4587cd46a0d073bd9992bb93c306d366f07cda2391)
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument allowed_audience", value=allowed_audience, expected_type=type_hints["allowed_audience"])
                check_type(argname="argument allowed_clients", value=allowed_clients, expected_type=type_hints["allowed_clients"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_url": discovery_url,
            }
            if allowed_audience is not None:
                self._values["allowed_audience"] = allowed_audience
            if allowed_clients is not None:
                self._values["allowed_clients"] = allowed_clients

        @builtins.property
        def discovery_url(self) -> builtins.str:
            '''The configuration authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-discoveryurl
            '''
            result = self._values.get("discovery_url")
            assert result is not None, "Required property 'discovery_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents inbound authorization configuration options used to authenticate incoming requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedaudience
            '''
            result = self._values.get("allowed_audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_clients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents individual client IDs that are validated in the incoming JWT token validation process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedclients
            '''
            result = self._values.get("allowed_clients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomJWTAuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_mode": "networkMode",
            "network_mode_config": "networkModeConfig",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_mode: builtins.str,
            network_mode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRuntime.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The network configuration for the agent.

            :param network_mode: The network mode.
            :param network_mode_config: Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                network_configuration_property = bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                    network_mode="networkMode",
                
                    # the properties below are optional
                    network_mode_config=bedrockagentcore.CfnRuntime.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7ef3688e7eda46e5ab607f7c059dd5ed308816790e532f38188518d3a7c9b0f)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
                check_type(argname="argument network_mode_config", value=network_mode_config, expected_type=type_hints["network_mode_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }
            if network_mode_config is not None:
                self._values["network_mode_config"] = network_mode_config

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''The network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html#cfn-bedrockagentcore-runtime-networkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_mode_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.VpcConfigProperty"]]:
            '''Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html#cfn-bedrockagentcore-runtime-networkconfiguration-networkmodeconfig
            '''
            result = self._values.get("network_mode_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRuntime.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Network mode configuration for VPC.

            :param security_groups: Security groups for VPC.
            :param subnets: Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                vpc_config_property = bedrockagentcore.CfnRuntime.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3e546c3d4da6e03e6ff8e890d2d32819d3e7c17149a4f17d0e75c9569fa3aad9)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''Security groups for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-vpcconfig.html#cfn-bedrockagentcore-runtime-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-vpcconfig.html#cfn-bedrockagentcore-runtime-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.WorkloadIdentityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"workload_identity_arn": "workloadIdentityArn"},
    )
    class WorkloadIdentityDetailsProperty:
        def __init__(self, *, workload_identity_arn: builtins.str) -> None:
            '''The workload identity details for the agent.

            :param workload_identity_arn: The Amazon Resource Name (ARN) for the workload identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                workload_identity_details_property = bedrockagentcore.CfnRuntime.WorkloadIdentityDetailsProperty(
                    workload_identity_arn="workloadIdentityArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68380bfa2496b392a6192eeab7bae5b15e67d93a4946dff9481dca7e2b9da401)
                check_type(argname="argument workload_identity_arn", value=workload_identity_arn, expected_type=type_hints["workload_identity_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workload_identity_arn": workload_identity_arn,
            }

        @builtins.property
        def workload_identity_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the workload identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html#cfn-bedrockagentcore-runtime-workloadidentitydetails-workloadidentityarn
            '''
            result = self._values.get("workload_identity_arn")
            assert result is not None, "Required property 'workload_identity_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkloadIdentityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IRuntimeEndpointRef, _ITaggableV2_4e6798f8)
class CfnRuntimeEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeEndpoint",
):
    '''AgentCore Runtime is a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools using any open-source framework including LangGraph, CrewAI, and Strands Agents, any protocol, and any model.

    For more information about using agent runtime endpoints in Amazon Bedrock AgentCore, see `AgentCore Runtime versioning and endpoints <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-runtime-versioning.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html
    :cloudformationResource: AWS::BedrockAgentCore::RuntimeEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_runtime_endpoint = bedrockagentcore.CfnRuntimeEndpoint(self, "MyCfnRuntimeEndpoint",
            agent_runtime_id="agentRuntimeId",
            name="name",
        
            # the properties below are optional
            agent_runtime_version="agentRuntimeVersion",
            description="description",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        agent_runtime_id: builtins.str,
        name: builtins.str,
        agent_runtime_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_runtime_id: The agent runtime ID.
        :param name: The name of the AgentCore Runtime endpoint.
        :param agent_runtime_version: The version of the agent.
        :param description: Contains information about an agent runtime endpoint. An agent runtime is the execution environment for a Amazon Bedrock Agent.
        :param tags: The tags for the AgentCore Runtime endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f889c0edf8dd4715192bf69e6433f02f671ca35ed9b8e8f7622b298a7b14955a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuntimeEndpointProps(
            agent_runtime_id=agent_runtime_id,
            name=name,
            agent_runtime_version=agent_runtime_version,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e6a578bb33afa13fb1d85d1b682fc96e67f21a5fb168de296365084e02f261)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91be73ce07416705255e5e1569db31b3f488f1376320ddae8d8803981071f602)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeArn")
    def attr_agent_runtime_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the runtime agent.

        :cloudformationAttribute: AgentRuntimeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeEndpointArn")
    def attr_agent_runtime_endpoint_arn(self) -> builtins.str:
        '''The endpoint Amazon Resource Name (ARN).

        :cloudformationAttribute: AgentRuntimeEndpointArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeEndpointArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the endpoint was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the memory is in a failed state.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the runtime endpoint.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the endpoint was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLiveVersion")
    def attr_live_version(self) -> builtins.str:
        '''The live version for the runtime endpoint.

        :cloudformationAttribute: LiveVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLiveVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the runtime endpoint.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetVersion")
    def attr_target_version(self) -> builtins.str:
        '''The target version.

        :cloudformationAttribute: TargetVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetVersion"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> RuntimeEndpointReference:
        '''A reference to a RuntimeEndpoint resource.'''
        return typing.cast(RuntimeEndpointReference, jsii.get(self, "runtimeEndpointRef"))

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeId")
    def agent_runtime_id(self) -> builtins.str:
        '''The agent runtime ID.'''
        return typing.cast(builtins.str, jsii.get(self, "agentRuntimeId"))

    @agent_runtime_id.setter
    def agent_runtime_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ceb50df9e5593b49d2fbdc6aac8e77c6be9322ee82ceea79d7d86478e1a9d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f380de6caf6e91bd3b0399e46b356f219d19dd4297d832ed74437f4653be82c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeVersion")
    def agent_runtime_version(self) -> typing.Optional[builtins.str]:
        '''The version of the agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentRuntimeVersion"))

    @agent_runtime_version.setter
    def agent_runtime_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c0052c9218918d9940523a8d7f016f7eaf5fe73a714ee05b2ba7a94aa9df9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Contains information about an agent runtime endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479a4b8aa6bb0db70941c7bc7a41e153fdbf533d62d2c2dc2ae2edf57fb46e99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the AgentCore Runtime endpoint.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df913b08f181c8777324479d4caab3dc1c0e41137ac1db4a0b10f478ad63ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "BrowserCustomReference",
    "CfnBrowserCustom",
    "CfnBrowserCustomProps",
    "CfnCodeInterpreterCustom",
    "CfnCodeInterpreterCustomProps",
    "CfnGateway",
    "CfnGatewayProps",
    "CfnGatewayTarget",
    "CfnGatewayTargetProps",
    "CfnMemory",
    "CfnMemoryProps",
    "CfnRuntime",
    "CfnRuntimeEndpoint",
    "CfnRuntimeEndpointProps",
    "CfnRuntimeProps",
    "CodeInterpreterCustomReference",
    "GatewayReference",
    "GatewayTargetReference",
    "IBrowserCustomRef",
    "ICodeInterpreterCustomRef",
    "IGatewayRef",
    "IGatewayTargetRef",
    "IMemoryRef",
    "IRuntimeEndpointRef",
    "IRuntimeRef",
    "MemoryReference",
    "RuntimeEndpointReference",
    "RuntimeReference",
]

publication.publish()

def _typecheckingstub__45e545da2b3da370563839cf7802f81e77f186bac4ddee7d944e49364fcf8806(
    *,
    browser_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f9adb5e20b52bbdc47438decbd54e3ebb4b1976cbf46432a19597fc6589c39(
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5217aa9ccd0ec964b92c3a48855bb1494914c435606fcee5b0faefd790d264(
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790df6c55e75e75d6f8c8a9a5518586d5e4ae350e3bfc4555e2ed4bf3c572f31(
    *,
    authorizer_type: builtins.str,
    name: builtins.str,
    protocol_type: builtins.str,
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    exception_level: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    protocol_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367178269f9a78c89b5ba5e07b10a309050b4b3eaefd55c5ee6f30ddad20209f(
    *,
    credential_provider_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.CredentialProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    target_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    gateway_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28dda218e5909d8e89c4ab4ee9bac6335e1f1cde1c399e1ac3c1c739ece89e19(
    *,
    event_expiry_duration: jsii.Number,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    memory_execution_role_arn: typing.Optional[builtins.str] = None,
    memory_strategies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.MemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03746d507f3e8e95afbebc436c73d1ac1fc643ccea60f817b99b76cb41ccf5fb(
    *,
    agent_runtime_id: builtins.str,
    name: builtins.str,
    agent_runtime_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e489b12cef85647a902e6bba6db3bf5f3ef1a856b74cf0fc5a7f8d1d0fa4a4b(
    *,
    agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AgentRuntimeArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    agent_runtime_name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    protocol_configuration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89dc37aef7efb202707ab991eff3008383de6de10f2228d9e9beb350d3f170d5(
    *,
    code_interpreter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4e6eebff32fea6f708a0bdf21025e0a9500bd2a3cdfdda828c784ebacee92ec(
    *,
    gateway_arn: builtins.str,
    gateway_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b0f80d3aca56f187d6dce631a5608c1969f75cc45ffbb5433808d3f24b64e6(
    *,
    gateway_identifier: builtins.str,
    target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b3fcbed21b451e3876962b07eac0b89aa927286825f06a266f1378a2f1b0f1(
    *,
    memory_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056e5ef22e335ff5e02bdd57f3e564e80393e99c891cc1890f945dd001ef5b8f(
    *,
    agent_runtime_endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8847701d5ac2ffc328a04478df4877176577ccf780cdf31ccc35b7d9bbcc331a(
    *,
    agent_runtime_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e817ad5ee6496ab54cf569758c4d73da62a4d6f5cf0c34866960f6e4677343e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5d38dc7619d36a2a4f39c13ec237b55f560a41ac9a162b787880e8e6ba2f47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    browser_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12637c5685b21eb50c5acd05eb9308d8266fc2816549a6a2816d9399823e8551(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14f4b2516dbe32242e98828488dc4abcc900e39ac20507ae2fd0d16a3a0457c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c7dc0414899a74bed53146d246f036f214f82b031723849419726e12bcee67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89dfccc35ccd0a377234eb3e008038ad66200df7a4f3c63bf61ebf273a7f42e(
    value: typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.BrowserNetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16faa304c4f18b8bba1ee70b209c47d9944346a1e88926b4ee4ea5fe723fd64(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd292342e1165d23c8ce68a72d30c745d42a2586b394e8bcb4aa1ec13e9cc74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089c5a25d69d7c7abf4193f45206b584472351088cbe92835bb014923a48f2e7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.RecordingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e813ff9c64c23f175682396c7a13b02b9193809d3629b73f2ecac10192c8c2(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d5bebf1ad5159cc9014318eaa4c540145c82225bd9e29170035b0a29d0ee07(
    *,
    network_mode: builtins.str,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754929ea2dabad59807821380b38b3ef1b1955a5473f5469b18a7dcc81600948(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6787b09f9e077c274ab79cdf45ea5157eec8aea8960e77f8e128fab67b3cbc26(
    *,
    bucket: builtins.str,
    prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46efbe5ee20e23cd9dc9ee29c1cd041e741b8a0aeb2c0ea76ed3cb6cab180dad(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aaa167a6af98d626969b5bd2de9377658de4e8d04df0b48dc5916f9e503a029(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e6193c6a8378455a4decc0c525a09a78674fd7ad426e58017e57035bc1789a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    code_interpreter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4b7a28e87b1af264773dfddc0e9da46bb99c921aa85fb942fcc7ca03680597(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6d68ae9ee508df2d25ca9f4fa9a800c1215c05ac37929135ce20e393a44113(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58fa8bcb0ec87d3b6f75396018d3eeff06205adbf6ade289f0ac1710d71c909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36911cef74e5cac559eb0b558b639739fba4dccbbc8a224553a0f0a0cace3cd(
    value: typing.Union[_IResolvable_da3f097b, CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33607ff407017e2c7ecefbc727c6f7660550a46fe6b356799810d75ccf8d662(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597443cc8b5cdaed2db807a1545702d23f8f925435f13cd3d17111236aba2428(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466065bbc5e5f3997568d60c567b51bbc4a9a4900e6ce6da9f9499f85329a3a4(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae1295735d5d0996afa02b88ef9dddbd193fc77b25f7b69433fd57c1240bb3a(
    *,
    network_mode: builtins.str,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c8e6007d5911afbd85662033d4936d1846dbfdc6caa2fb2e69de26653ccc32(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__718d4d7128ca57b0228b268f1204c5574e63e51d4e7701a53fd67a1e8ec17c63(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorizer_type: builtins.str,
    name: builtins.str,
    protocol_type: builtins.str,
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    exception_level: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    protocol_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1253940d92e3f35d08808461458766f65528b0878c674311aabd74aa0a76ce30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e1eb8798612291b5b13aae1ac0d9cb4513c21df38593628be4d5e2fe660886(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3733b65f293d2d9f1304c9c6a4cfd4c4aa4a9dca54f65a221b403a9fa85809d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faac8d45eefa612f06e0139bc26af7005d13df5a552a63d10084bfbc444fd266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2ccf9c2c13ca5a79d82fee59155dfbaa87d3d17ccc1f27959c635732127d90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a750b424a29fb58f4f0dcc52028237d740f0b0b92d8420600048da5b20537f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c34ffb86639149c1c6323ad6aa1ec7b9f7d9e7f17a5f5306e5d67d30110ba83(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGateway.AuthorizerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89e3b58faac93b47a86d253bd377ccfed6b64d0088167686a5ce5a6f01bc27b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791936566b3e629fd378dc6a46c31b1a5134acc616fbd9ed9eebc092ed3be3e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d2d9d8c84164d38a9976889d155298546ea61a787e120117719ee748ac6cf6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05982d11a516cc3cf2e986a22173b4993c5267490c660a8f123f9c141f3f117b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayProtocolConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8136c8abfebcb699dd26d8e65dbb8e7a922f1cdc2f58375541b3436f139609a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__788309d24193b18115a31defebe9337a71550513b7163a4a603f72832a42ab79(
    *,
    custom_jwt_authorizer: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.CustomJWTAuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc4944f630bec36007bb93b09eab3e99763f1bed11457e642c0ab535144159e(
    *,
    discovery_url: builtins.str,
    allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381e09b484f23635acaed28352a759fdd9ac853b91ce6a848c9ed3892887eb7c(
    *,
    mcp: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.MCPGatewayConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caff723b1f8dc289e3e0d1f554fe16628873911a93ec8c36ed92f59cde7798c4(
    *,
    instructions: typing.Optional[builtins.str] = None,
    search_type: typing.Optional[builtins.str] = None,
    supported_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e940e88ca017f9ccde7a0419db94aaed6321cc4f2368ad6aa9fe229c8d1d8a3a(
    *,
    workload_identity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca4172cb2708dfeb7420a18b960df15915d2da8589b9495c034bd700c3bd768(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    credential_provider_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.CredentialProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    target_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    gateway_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facd54b7bb4cca942a82b0859b83ffbee83d2b5964da7507bd01ce76b51602d7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f55ddaf00701b9be96b4083ffcf99e108df2b912a7fa6a0930aacc493dc19b3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087a7adedbf9e4e0e6abc10f84df215c78eebc146c64c53668096978e91820bd(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGatewayTarget.CredentialProviderConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4fb979142cd31fef07a02c2a4b5e3d0eb49bf962781821346eac630d16fcc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d18e620b511ca77468615f894540073998d43a19f84c7bd4555618e80c9a3d(
    value: typing.Union[_IResolvable_da3f097b, CfnGatewayTarget.TargetConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88eae40375f8237511c7176b5010bb5247cb77ff6160f37b46d60eac254c2403(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c9f5798e9b6c54f5080d4aef35f1a5d286541a90ad283e95cae82b7a8e7de1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33b2b3f3a682c83f92cbd3e15b4552ff1592eb43e06b8e26d9bb1e8f1003ecd(
    *,
    provider_arn: builtins.str,
    credential_location: typing.Optional[builtins.str] = None,
    credential_parameter_name: typing.Optional[builtins.str] = None,
    credential_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309e9dda1e6dfcce4b7777150028f4c6782bdc89a099f0ac87ab71e9967a8277(
    *,
    inline_payload: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.S3ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149dd633d64001d8edf5b8db5417ed0fc1bfaecff9240452d6911051ec05238e(
    *,
    credential_provider_type: builtins.str,
    credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.CredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db13937427760cb24e319f55daf7a1b38d00d0bb009b7b145665b608c53b0f5c(
    *,
    api_key_credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiKeyCredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    oauth_credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.OAuthCredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ba80f262600990b7647765d60a5f51fb86eeeaf8708f22bc73e4794e784785(
    *,
    lambda_arn: builtins.str,
    tool_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ToolSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b1d88210caa384ede03a06bee42d13165c8bf4cc4206a236d795c44da216e3c(
    *,
    lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.McpLambdaTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_api_schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiSchemaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    smithy_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiSchemaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c602c1e6012421bcbacb23364333a8030b673b0a8e3ebad72fba42b295c2f64(
    *,
    provider_arn: builtins.str,
    scopes: typing.Sequence[builtins.str],
    custom_parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0b1feb9921a2069b72a9a314cb583fbbc6b6fc8af438b2e8f420e03d0368f7(
    *,
    bucket_owner_account_id: typing.Optional[builtins.str] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc512741cd348cf43b33e4ea0df31aae8766e6990dc0675d9111d9a7eb5f9c6a(
    *,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    items: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    required: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a64335e118208df2b03631e56ce84dab935a9d2c9dee1c27c584de679d4dcd6(
    *,
    mcp: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.McpTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c9a8204fd6db934022c917c4dc62346cf5269b544292d1bac5ed2aae995a300(
    *,
    description: builtins.str,
    input_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    output_schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff8fed96fdad56eb717513408b41cd94cf1c34461313bbb4de520c38aeab416(
    *,
    inline_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ToolDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.S3ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b95a7255db9df73ca225a32aecd624481667f18f3308ba77ce3fbf7d7e1cf4f0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_expiry_duration: jsii.Number,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    memory_execution_role_arn: typing.Optional[builtins.str] = None,
    memory_strategies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.MemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b76cbb12d67c915a322289eef0caf05911a64361531f525f945065e6fbd1b0b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29efd6b6b9a6ac1e7281cd85ae63e9d6002789f18830f68a7cec0a0d012ac382(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c376bc3bd26c18cf626509568f040ac75ef52a68ef8a39ca3e5b6b8308374496(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f948061bc9aba0eb248f047c217bd96c19cf47d09da3c7b9708380caf387394f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93e29c7f80206ddbc4de97f028b669d82daf8dd5c65b29ae535035b57cd461ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b682a270f87cf6f76b16e70568b3e20c1994f4ff375efed9e59f3ff29cce80cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd6b17fbf9c4464799eba94f4be79124e7c5491b62da83c1a8bd39d6f2a0def(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18515e6738d6694af7855ee5a84c8940fcfa482c5e51f03ea9e0abda4a56765(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMemory.MemoryStrategyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20937c3b9ee32cb1df4d7eaf09c5da2b921076b8dab073c8f61380cb9b64e33b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b393ad440afaf6b639d0ad3fdd1431e23bc8fa4658d92c51bbe3ae892ec72e(
    *,
    self_managed_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SelfManagedConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    semantic_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    summary_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SummaryOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_preference_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f9ef2809f813258bef3dcd9ec460d2f237f2127d9f7cb9aae3256166ba8183(
    *,
    name: builtins.str,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.CustomConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e7fa751a69795001dc84cc0fd23b36ae6952ce8c475d549b7599b3353a7c9a(
    *,
    payload_delivery_bucket_name: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7fa25b2413ebaf6794a4e0d96d4404f578a37b86cd501369f7c93f8d049e8e7(
    *,
    custom_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.CustomMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    semantic_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    summary_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SummaryMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_preference_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26f0bfb6bb91a96529926b34610d43ded0571d826aa8ac6cb6e63367e9ea089(
    *,
    message_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4fcd7b9f7c5c0bb0c80ff54635936b78ada2b3d24596ba7cd43b9ece93f804c(
    *,
    historical_context_window_size: typing.Optional[jsii.Number] = None,
    invocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.InvocationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trigger_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.TriggerConditionInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdd1426fa7487dcb02499d9f810acd963031578a3c30fd4be0b076b09a32b124(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393b5baf9d5b39c6498ec7dde998e56d10f272578b90e6901d6e5717c4d0b79d(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669cd3ffc171b2cd7f3a4c3d6196e5a075449bedd07119892324a275601cf283(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fcd9046e68a8e9401f48408f0a4870f5c13f714c342e2085d178557990c4ee(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticOverrideExtractionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee517e4354bf11f650f3de6c9e3789b5ced3c958c97582b32deda0a2643b376(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c990b6378d188092fe95d78caab0eb586836dc0ca2194f9cbf3788c24c6ec053(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23ed198bcd958ec3a014c4dd2d6c418b82bc1895ca1b0af24503f002e61d492(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf65bf0b7de7a122f8fdf3c50a61ba88dd5248ad841dd004cb6bd0f7174ec45(
    *,
    idle_session_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171b0765936a13c6e7c17456605ec3e2bc9c36685a864e8c11187bfd9a4bc89a(
    *,
    token_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca3b096b467bf1778a21961da57f12ce16cf0ef63aeee1b912577f66fdb48cb(
    *,
    message_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.MessageBasedTriggerInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.TimeBasedTriggerInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    token_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.TokenBasedTriggerInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404072c850abd871eb86ee8d04d20a311da6fb4147c983194a800b234cbf1e04(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf5e9da18deac0b8b6ae4a435ef031fafc5037acda6e9b5a2f31d25335ea0ad(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2496eed790ccc12ab395eda9327489aa843786babbb42e3d6238d462a4c629(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a657a70bb10847e586abd34f2ecc11ddcafa4b88002f03b52b85d085202adcfd(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f75c2b58380182b53165109480fecdbf9bcd35c2fcfcfea5141466ba05b7e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AgentRuntimeArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    agent_runtime_name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    protocol_configuration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41eb1aeeb420a432d00eafdf7061763658f434f8c1b3fac5748e0b80cf168cda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbc19212156590bcfcec54a917d56095cf1d0e95a1f4f4107501a8cf457feb7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afa965e1f7852c99b813a59ddc326e4e8b2e629273fff790e48abcc309421fb(
    value: typing.Union[_IResolvable_da3f097b, CfnRuntime.AgentRuntimeArtifactProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e5f3a5d4d3f3cf24f87565ebb2f7c531ed9e006970eb5a59dee4eeed670f19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a3b80aa643920bb76e97b49e6d7c54f3367df4203a420045d6d631a4d54658(
    value: typing.Union[_IResolvable_da3f097b, CfnRuntime.NetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712719ad084eaaa1f88407e6da1dd4ed68fa570a04329676de9d476fde02ebfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577d498b775175712bf02d50d4dc0a7fa74d069187c6c0daba641442a844c29e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuntime.AuthorizerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86887c96ad11d54aa9be7288cd5dfe9a9b3cb370236b2cf8c98f0ea09d7246e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b52f571e16cbee3d0cb6aef888169b2fdf172a92199c29075b1bbfe5eb3091(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd16ca9a4cf1077fb69bea991264277b990667565406b724c960232073239095(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c0ee18c00618ce3d55cf861e88265d3db540867ff55146671310649d3ccaee(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51346444ae527a839c6fcfd4fd456eeea9b11da43bf9dadd9b152cfc716ecfd2(
    *,
    container_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.ContainerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb18338480d08b211086521e0155635de6c3b54cf6ebbb5a7ee690c697991b4b(
    *,
    custom_jwt_authorizer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.CustomJWTAuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0740ce1d3425c4e128b2f49784ee2a02ae6e81129ade5290d001575f4ecacb8(
    *,
    container_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6479ff33c6925aa85dcd6d4587cd46a0d073bd9992bb93c306d366f07cda2391(
    *,
    discovery_url: builtins.str,
    allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ef3688e7eda46e5ab607f7c059dd5ed308816790e532f38188518d3a7c9b0f(
    *,
    network_mode: builtins.str,
    network_mode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e546c3d4da6e03e6ff8e890d2d32819d3e7c17149a4f17d0e75c9569fa3aad9(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68380bfa2496b392a6192eeab7bae5b15e67d93a4946dff9481dca7e2b9da401(
    *,
    workload_identity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f889c0edf8dd4715192bf69e6433f02f671ca35ed9b8e8f7622b298a7b14955a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_runtime_id: builtins.str,
    name: builtins.str,
    agent_runtime_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e6a578bb33afa13fb1d85d1b682fc96e67f21a5fb168de296365084e02f261(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91be73ce07416705255e5e1569db31b3f488f1376320ddae8d8803981071f602(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ceb50df9e5593b49d2fbdc6aac8e77c6be9322ee82ceea79d7d86478e1a9d74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f380de6caf6e91bd3b0399e46b356f219d19dd4297d832ed74437f4653be82c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c0052c9218918d9940523a8d7f016f7eaf5fe73a714ee05b2ba7a94aa9df9f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479a4b8aa6bb0db70941c7bc7a41e153fdbf533d62d2c2dc2ae2edf57fb46e99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df913b08f181c8777324479d4caab3dc1c0e41137ac1db4a0b10f478ad63ce7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBrowserCustomRef, ICodeInterpreterCustomRef, IGatewayRef, IGatewayTargetRef, IMemoryRef, IRuntimeEndpointRef, IRuntimeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
