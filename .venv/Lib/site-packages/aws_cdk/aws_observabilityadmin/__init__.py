r'''
# AWS::ObservabilityAdmin Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_observabilityadmin as observabilityadmin
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ObservabilityAdmin construct libraries](https://constructs.dev/search?q=observabilityadmin)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ObservabilityAdmin resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ObservabilityAdmin.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ObservabilityAdmin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ObservabilityAdmin.html).

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnOrganizationCentralizationRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationCentralizationRule``.

        :param rule: 
        :param rule_name: The name of the organization centralization rule.
        :param tags: A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see `What are tags? <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_organization_centralization_rule_props = observabilityadmin.CfnOrganizationCentralizationRuleProps(
                rule=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty(
                    destination=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                        region="region",
            
                        # the properties below are optional
                        account="account",
                        destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                            backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                                region="region",
            
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            ),
                            logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                                encryption_strategy="encryptionStrategy",
            
                                # the properties below are optional
                                encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                                kms_key_arn="kmsKeyArn"
                            )
                        )
                    ),
                    source=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                        regions=["regions"],
            
                        # the properties below are optional
                        scope="scope",
                        source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                            encrypted_log_group_strategy="encryptedLogGroupStrategy",
                            log_group_selection_criteria="logGroupSelectionCriteria"
                        )
                    )
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00d0ecee2cd9ac728ca3e321203ce2e611e56b0b2d415ba2673a50599e4512cd)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleProperty"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair to filter resources based on tags associated with the resource.

        For more information about tags, see `What are tags? <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationCentralizationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnOrganizationTelemetryRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationTelemetryRule``.

        :param rule: The name of the organization telemetry rule.
        :param rule_name: The name of the organization centralization rule.
        :param tags: Lists all tags attached to the specified telemetry rule resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_organization_telemetry_rule_props = observabilityadmin.CfnOrganizationTelemetryRuleProps(
                rule=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
            
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    scope="scope",
                    selection_criteria="selectionCriteria"
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c94381428dd096d5bd5b31c1a78b0ec6c66b125c46a889f389e957dbf9f76b)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"]:
        '''The name of the organization telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Lists all tags attached to the specified telemetry rule resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationTelemetryRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnTelemetryRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTelemetryRule``.

        :param rule: Retrieves the details of a specific telemetry rule in your account.
        :param rule_name: The name of the telemetry rule.
        :param tags: Lists all tags attached to the specified telemetry rule resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_telemetry_rule_props = observabilityadmin.CfnTelemetryRuleProps(
                rule=observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
            
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    selection_criteria="selectionCriteria"
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7455cb845b044ed569a8ec8407abf811920062f00d1e54ad191e90dc9b7e2811)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"]:
        '''Retrieves the details of a specific telemetry rule in your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Lists all tags attached to the specified telemetry rule resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTelemetryRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.IOrganizationCentralizationRuleRef"
)
class IOrganizationCentralizationRuleRef(
    _constructs_77d1e7e8.IConstruct,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationCentralizationRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationCentralizationRuleRef")
    def organization_centralization_rule_ref(
        self,
    ) -> "OrganizationCentralizationRuleReference":
        '''(experimental) A reference to a OrganizationCentralizationRule resource.

        :stability: experimental
        '''
        ...


class _IOrganizationCentralizationRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationCentralizationRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_observabilityadmin.IOrganizationCentralizationRuleRef"

    @builtins.property
    @jsii.member(jsii_name="organizationCentralizationRuleRef")
    def organization_centralization_rule_ref(
        self,
    ) -> "OrganizationCentralizationRuleReference":
        '''(experimental) A reference to a OrganizationCentralizationRule resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationCentralizationRuleReference", jsii.get(self, "organizationCentralizationRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationCentralizationRuleRef).__jsii_proxy_class__ = lambda : _IOrganizationCentralizationRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.IOrganizationTelemetryRuleRef"
)
class IOrganizationTelemetryRuleRef(
    _constructs_77d1e7e8.IConstruct,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationTelemetryRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationTelemetryRuleRef")
    def organization_telemetry_rule_ref(self) -> "OrganizationTelemetryRuleReference":
        '''(experimental) A reference to a OrganizationTelemetryRule resource.

        :stability: experimental
        '''
        ...


class _IOrganizationTelemetryRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationTelemetryRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_observabilityadmin.IOrganizationTelemetryRuleRef"

    @builtins.property
    @jsii.member(jsii_name="organizationTelemetryRuleRef")
    def organization_telemetry_rule_ref(self) -> "OrganizationTelemetryRuleReference":
        '''(experimental) A reference to a OrganizationTelemetryRule resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationTelemetryRuleReference", jsii.get(self, "organizationTelemetryRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationTelemetryRuleRef).__jsii_proxy_class__ = lambda : _IOrganizationTelemetryRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_observabilityadmin.ITelemetryRuleRef")
class ITelemetryRuleRef(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''(experimental) Indicates that this resource can be referenced as a TelemetryRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="telemetryRuleRef")
    def telemetry_rule_ref(self) -> "TelemetryRuleReference":
        '''(experimental) A reference to a TelemetryRule resource.

        :stability: experimental
        '''
        ...


class _ITelemetryRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TelemetryRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_observabilityadmin.ITelemetryRuleRef"

    @builtins.property
    @jsii.member(jsii_name="telemetryRuleRef")
    def telemetry_rule_ref(self) -> "TelemetryRuleReference":
        '''(experimental) A reference to a TelemetryRule resource.

        :stability: experimental
        '''
        return typing.cast("TelemetryRuleReference", jsii.get(self, "telemetryRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITelemetryRuleRef).__jsii_proxy_class__ = lambda : _ITelemetryRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.OrganizationCentralizationRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class OrganizationCentralizationRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a OrganizationCentralizationRule resource.

        :param rule_arn: The RuleArn of the OrganizationCentralizationRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            organization_centralization_rule_reference = observabilityadmin.OrganizationCentralizationRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b3ad11b09d25a384211da640f6a09bc1e0c17db4ccd5b1f32b27309ce4215f5)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the OrganizationCentralizationRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationCentralizationRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.OrganizationTelemetryRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class OrganizationTelemetryRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a OrganizationTelemetryRule resource.

        :param rule_arn: The RuleArn of the OrganizationTelemetryRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            organization_telemetry_rule_reference = observabilityadmin.OrganizationTelemetryRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__546326e4a1c8218daecae9d95475d22bf60d95f4d5ec20cd304d51ba67eb92f4)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the OrganizationTelemetryRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationTelemetryRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.TelemetryRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class TelemetryRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a TelemetryRule resource.

        :param rule_arn: The RuleArn of the TelemetryRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            telemetry_rule_reference = observabilityadmin.TelemetryRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e5c59e1cd03c9d8825ebf008d30354018de9d95b37c45267b93575de094bcfc)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the TelemetryRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetryRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, IOrganizationCentralizationRuleRef, _ITaggableV2_4e6798f8)
class CfnOrganizationCentralizationRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule",
):
    '''Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::OrganizationCentralizationRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_organization_centralization_rule = observabilityadmin.CfnOrganizationCentralizationRule(self, "MyCfnOrganizationCentralizationRule",
            rule=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty(
                destination=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                    region="region",
        
                    # the properties below are optional
                    account="account",
                    destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                        backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                            region="region",
        
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        ),
                        logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                            encryption_strategy="encryptionStrategy",
        
                            # the properties below are optional
                            encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                ),
                source=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                    regions=["regions"],
        
                    # the properties below are optional
                    scope="scope",
                    source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                        encrypted_log_group_strategy="encryptedLogGroupStrategy",
                        log_group_selection_criteria="logGroupSelectionCriteria"
                    )
                )
            ),
            rule_name="ruleName",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: 
        :param rule_name: The name of the organization centralization rule.
        :param tags: A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see `What are tags? <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html>`_
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18acbc8917f3c4cbc8bb06f5fae76010e41ab5f0e9b157f4c324c214a180ef2e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationCentralizationRuleProps(
            rule=rule, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02b2ea8ec552fc96b3662b368fa64eea5f82839c3bd0f1aa52bd64bc495f5341)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f130448a4f76aff49b8e31a382ea5ab14eacdf34a74afe86be23352ded6622e1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the organization centralization rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="organizationCentralizationRuleRef")
    def organization_centralization_rule_ref(
        self,
    ) -> OrganizationCentralizationRuleReference:
        '''A reference to a OrganizationCentralizationRule resource.'''
        return typing.cast(OrganizationCentralizationRuleReference, jsii.get(self, "organizationCentralizationRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fbb5a84b6997cee28db4665d22fee83629861a1e51fe754b85b3858441e7c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42b1edd10be1da3c565db5f9585850487a7c51b5ad7ab0a72c1d4345b4ac7f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair to filter resources based on tags associated with the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58679a9a3a800195cc0ecf82553695580c2dd2061901e27320b9025cb6ed262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "account": "account",
            "destination_logs_configuration": "destinationLogsConfiguration",
        },
    )
    class CentralizationRuleDestinationProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            account: typing.Optional[builtins.str] = None,
            destination_logs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying the primary destination for centralized telemetry data.

            :param region: The primary destination region to which telemetry data should be centralized.
            :param account: The destination account (within the organization) to which the telemetry data should be centralized.
            :param destination_logs_configuration: Log specific configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                centralization_rule_destination_property = observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                    region="region",
                
                    # the properties below are optional
                    account="account",
                    destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                        backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                            region="region",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        ),
                        logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                            encryption_strategy="encryptionStrategy",
                
                            # the properties below are optional
                            encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48736d0ec2563919af9b82675cbe965d2288bd15210b9c8b34911e7a89ae0f47)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument account", value=account, expected_type=type_hints["account"])
                check_type(argname="argument destination_logs_configuration", value=destination_logs_configuration, expected_type=type_hints["destination_logs_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if account is not None:
                self._values["account"] = account
            if destination_logs_configuration is not None:
                self._values["destination_logs_configuration"] = destination_logs_configuration

        @builtins.property
        def region(self) -> builtins.str:
            '''The primary destination region to which telemetry data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account(self) -> typing.Optional[builtins.str]:
            '''The destination account (within the organization) to which the telemetry data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-account
            '''
            result = self._values.get("account")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_logs_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty"]]:
            '''Log specific configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationlogsconfiguration
            '''
            result = self._values.get("destination_logs_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CentralizationRuleDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class CentralizationRuleProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

            :param destination: Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.
            :param source: Configuration determining the source of the telemetry data to be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                centralization_rule_property = observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty(
                    destination=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                        region="region",
                
                        # the properties below are optional
                        account="account",
                        destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                            backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                                region="region",
                
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            ),
                            logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                                encryption_strategy="encryptionStrategy",
                
                                # the properties below are optional
                                encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                                kms_key_arn="kmsKeyArn"
                            )
                        )
                    ),
                    source=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                        regions=["regions"],
                
                        # the properties below are optional
                        scope="scope",
                        source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                            encrypted_log_group_strategy="encryptedLogGroupStrategy",
                            log_group_selection_criteria="logGroupSelectionCriteria"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb475427ce4a2316b8478f1c58d17ddd5783412b26cdfb98819c47313aa718dc)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "source": source,
            }

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty"]:
            '''Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty"], result)

        @builtins.property
        def source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty"]:
            '''Configuration determining the source of the telemetry data to be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CentralizationRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "regions": "regions",
            "scope": "scope",
            "source_logs_configuration": "sourceLogsConfiguration",
        },
    )
    class CentralizationRuleSourceProperty:
        def __init__(
            self,
            *,
            regions: typing.Sequence[builtins.str],
            scope: typing.Optional[builtins.str] = None,
            source_logs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying the source of telemetry data to be centralized.

            :param regions: The list of source regions from which telemetry data should be centralized.
            :param scope: The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.
            :param source_logs_configuration: Log specific configuration for centralization source log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                centralization_rule_source_property = observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                    regions=["regions"],
                
                    # the properties below are optional
                    scope="scope",
                    source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                        encrypted_log_group_strategy="encryptedLogGroupStrategy",
                        log_group_selection_criteria="logGroupSelectionCriteria"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c4d1dff0252b97263e138c77bea2f698277762eeffd4fcf3911e496ac5762e4)
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument source_logs_configuration", value=source_logs_configuration, expected_type=type_hints["source_logs_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "regions": regions,
            }
            if scope is not None:
                self._values["scope"] = scope
            if source_logs_configuration is not None:
                self._values["source_logs_configuration"] = source_logs_configuration

        @builtins.property
        def regions(self) -> typing.List[builtins.str]:
            '''The list of source regions from which telemetry data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-regions
            '''
            result = self._values.get("regions")
            assert result is not None, "Required property 'regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def scope(self) -> typing.Optional[builtins.str]:
            '''The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-scope
            '''
            result = self._values.get("scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_logs_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty"]]:
            '''Log specific configuration for centralization source log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcelogsconfiguration
            '''
            result = self._values.get("source_logs_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CentralizationRuleSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_configuration": "backupConfiguration",
            "logs_encryption_configuration": "logsEncryptionConfiguration",
        },
    )
    class DestinationLogsConfigurationProperty:
        def __init__(
            self,
            *,
            backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            logs_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for centralization destination log groups, including encryption and backup settings.

            :param backup_configuration: Configuration defining the backup region and an optional KMS key for the backup destination.
            :param logs_encryption_configuration: The encryption configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                destination_logs_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                    backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                        region="region",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    ),
                    logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                        encryption_strategy="encryptionStrategy",
                
                        # the properties below are optional
                        encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5dd7a39f2c94fa5f25cdcfc83cd888a8c3b22c09afa009f3ed5de76fd5befe41)
                check_type(argname="argument backup_configuration", value=backup_configuration, expected_type=type_hints["backup_configuration"])
                check_type(argname="argument logs_encryption_configuration", value=logs_encryption_configuration, expected_type=type_hints["logs_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if backup_configuration is not None:
                self._values["backup_configuration"] = backup_configuration
            if logs_encryption_configuration is not None:
                self._values["logs_encryption_configuration"] = logs_encryption_configuration

        @builtins.property
        def backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty"]]:
            '''Configuration defining the backup region and an optional KMS key for the backup destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-backupconfiguration
            '''
            result = self._values.get("backup_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty"]], result)

        @builtins.property
        def logs_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty"]]:
            '''The encryption configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-logsencryptionconfiguration
            '''
            result = self._values.get("logs_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationLogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"region": "region", "kms_key_arn": "kmsKeyArn"},
    )
    class LogsBackupConfigurationProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for backing up centralized log data to a secondary region.

            :param region: Logs specific backup destination region within the primary destination account to which log data should be centralized.
            :param kms_key_arn: KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                logs_backup_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                    region="region",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35d26acca25f06381fb096b21a6f3791d0ef735549ac7bae5795f4e646184d86)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def region(self) -> builtins.str:
            '''Logs specific backup destination region within the primary destination account to which log data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogsBackupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_strategy": "encryptionStrategy",
            "encryption_conflict_resolution_strategy": "encryptionConflictResolutionStrategy",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class LogsEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_strategy: builtins.str,
            encryption_conflict_resolution_strategy: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for encrypting centralized log groups.

            This configuration is only applied to destination log groups for which the corresponding source log groups are encrypted using Customer Managed KMS Keys.

            :param encryption_strategy: Configuration that determines the encryption strategy of the destination log groups. CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.
            :param encryption_conflict_resolution_strategy: Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key. ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.
            :param kms_key_arn: KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                logs_encryption_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                    encryption_strategy="encryptionStrategy",
                
                    # the properties below are optional
                    encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d66f88a29d04606b9d6748d2a92fb0d7bf4a500a64fceff8556e1ac2275828e)
                check_type(argname="argument encryption_strategy", value=encryption_strategy, expected_type=type_hints["encryption_strategy"])
                check_type(argname="argument encryption_conflict_resolution_strategy", value=encryption_conflict_resolution_strategy, expected_type=type_hints["encryption_conflict_resolution_strategy"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_strategy": encryption_strategy,
            }
            if encryption_conflict_resolution_strategy is not None:
                self._values["encryption_conflict_resolution_strategy"] = encryption_conflict_resolution_strategy
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def encryption_strategy(self) -> builtins.str:
            '''Configuration that determines the encryption strategy of the destination log groups.

            CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionstrategy
            '''
            result = self._values.get("encryption_strategy")
            assert result is not None, "Required property 'encryption_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encryption_conflict_resolution_strategy(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key.

            ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionconflictresolutionstrategy
            '''
            result = self._values.get("encryption_conflict_resolution_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogsEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted_log_group_strategy": "encryptedLogGroupStrategy",
            "log_group_selection_criteria": "logGroupSelectionCriteria",
        },
    )
    class SourceLogsConfigurationProperty:
        def __init__(
            self,
            *,
            encrypted_log_group_strategy: builtins.str,
            log_group_selection_criteria: builtins.str,
        ) -> None:
            '''Configuration for selecting and handling source log groups for centralization.

            :param encrypted_log_group_strategy: A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK). ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.
            :param log_group_selection_criteria: The selection criteria that specifies which source log groups to centralize. The selection criteria uses the same format as OAM link filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                source_logs_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                    encrypted_log_group_strategy="encryptedLogGroupStrategy",
                    log_group_selection_criteria="logGroupSelectionCriteria"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20a12247cb1287e19ec3a764cc738d756d26c889450a5b771811f8378a2b5d6c)
                check_type(argname="argument encrypted_log_group_strategy", value=encrypted_log_group_strategy, expected_type=type_hints["encrypted_log_group_strategy"])
                check_type(argname="argument log_group_selection_criteria", value=log_group_selection_criteria, expected_type=type_hints["log_group_selection_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encrypted_log_group_strategy": encrypted_log_group_strategy,
                "log_group_selection_criteria": log_group_selection_criteria,
            }

        @builtins.property
        def encrypted_log_group_strategy(self) -> builtins.str:
            '''A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK).

            ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-encryptedloggroupstrategy
            '''
            result = self._values.get("encrypted_log_group_strategy")
            assert result is not None, "Required property 'encrypted_log_group_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_group_selection_criteria(self) -> builtins.str:
            '''The selection criteria that specifies which source log groups to centralize.

            The selection criteria uses the same format as OAM link filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-loggroupselectioncriteria
            '''
            result = self._values.get("log_group_selection_criteria")
            assert result is not None, "Required property 'log_group_selection_criteria' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceLogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, IOrganizationTelemetryRuleRef, _ITaggableV2_4e6798f8)
class CfnOrganizationTelemetryRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule",
):
    '''Retrieves the details of a specific organization centralization rule.

    This operation can only be called by the organization's management account or a delegated administrator account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::OrganizationTelemetryRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_organization_telemetry_rule = observabilityadmin.CfnOrganizationTelemetryRule(self, "MyCfnOrganizationTelemetryRule",
            rule=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                resource_type="resourceType",
                telemetry_type="telemetryType",
        
                # the properties below are optional
                destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                ),
                scope="scope",
                selection_criteria="selectionCriteria"
            ),
            rule_name="ruleName",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: The name of the organization telemetry rule.
        :param rule_name: The name of the organization centralization rule.
        :param tags: Lists all tags attached to the specified telemetry rule resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a67d6a9dd82924a413b7d3435faeb8efa735048df0244b926e672def8c2d5f75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationTelemetryRuleProps(
            rule=rule, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb893813673a29ee1f384593916d34bdcc440b816dfc54ad27097692c5a64e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c809c768027da00df4018694393faf5d77af9754b12923bf684ada119faecfc7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The arn of the organization telemetry rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="organizationTelemetryRuleRef")
    def organization_telemetry_rule_ref(self) -> OrganizationTelemetryRuleReference:
        '''A reference to a OrganizationTelemetryRule resource.'''
        return typing.cast(OrganizationTelemetryRuleReference, jsii.get(self, "organizationTelemetryRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"]:
        '''The name of the organization telemetry rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97cf84910a3c46b94c3e90ddf73c07b304a029e413bebd1b7c5e7b2bbe5cd411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84099afcf940dd46614099ecc03e181396a6d202813d1517bd79414c5aa2f5ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Lists all tags attached to the specified telemetry rule resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d494e45ec3f03fbc2168c2e374f689615e98524c832aa6247ad243fabe01ffe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_pattern": "destinationPattern",
            "destination_type": "destinationType",
            "retention_in_days": "retentionInDays",
            "vpc_flow_log_parameters": "vpcFlowLogParameters",
        },
    )
    class TelemetryDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            destination_pattern: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
            retention_in_days: typing.Optional[jsii.Number] = None,
            vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying where and how telemetry data should be delivered for AWS resources.

            :param destination_pattern: The pattern used to generate the destination path or name, supporting macros like and .
            :param destination_type: The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").
            :param retention_in_days: The number of days to retain the telemetry data in the destination.
            :param vpc_flow_log_parameters: Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_destination_configuration_property = observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36b4168c57b4555036ca598e8299a36985c9aab7a1eb6b84357df4454b340171)
                check_type(argname="argument destination_pattern", value=destination_pattern, expected_type=type_hints["destination_pattern"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
                check_type(argname="argument vpc_flow_log_parameters", value=vpc_flow_log_parameters, expected_type=type_hints["vpc_flow_log_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_pattern is not None:
                self._values["destination_pattern"] = destination_pattern
            if destination_type is not None:
                self._values["destination_type"] = destination_type
            if retention_in_days is not None:
                self._values["retention_in_days"] = retention_in_days
            if vpc_flow_log_parameters is not None:
                self._values["vpc_flow_log_parameters"] = vpc_flow_log_parameters

        @builtins.property
        def destination_pattern(self) -> typing.Optional[builtins.str]:
            '''The pattern used to generate the destination path or name, supporting macros like  and .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-destinationpattern
            '''
            result = self._values.get("destination_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retention_in_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain the telemetry data in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-retentionindays
            '''
            result = self._values.get("retention_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_flow_log_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty"]]:
            '''Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters
            '''
            result = self._values.get("vpc_flow_log_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "telemetry_type": "telemetryType",
            "destination_configuration": "destinationConfiguration",
            "scope": "scope",
            "selection_criteria": "selectionCriteria",
        },
    )
    class TelemetryRuleProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            telemetry_type: builtins.str,
            destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scope: typing.Optional[builtins.str] = None,
            selection_criteria: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines how telemetry should be configured for specific AWS resources.

            :param resource_type: The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC").
            :param telemetry_type: The type of telemetry to collect (Logs, Metrics, or Traces).
            :param destination_configuration: Configuration specifying where and how the telemetry data should be delivered.
            :param scope: The organizational scope to which the rule applies, specified using accounts or organizational units.
            :param selection_criteria: Criteria for selecting which resources the rule applies to, such as resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_rule_property = observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
                
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    scope="scope",
                    selection_criteria="selectionCriteria"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8febf24ebcbc00029972152d874df5e847a9f5cd45e05abb26e69f7a2cabc5bf)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument telemetry_type", value=telemetry_type, expected_type=type_hints["telemetry_type"])
                check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_type": resource_type,
                "telemetry_type": telemetry_type,
            }
            if destination_configuration is not None:
                self._values["destination_configuration"] = destination_configuration
            if scope is not None:
                self._values["scope"] = scope
            if selection_criteria is not None:
                self._values["selection_criteria"] = selection_criteria

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def telemetry_type(self) -> builtins.str:
            '''The type of telemetry to collect (Logs, Metrics, or Traces).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrytype
            '''
            result = self._values.get("telemetry_type")
            assert result is not None, "Required property 'telemetry_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty"]]:
            '''Configuration specifying where and how the telemetry data should be delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-destinationconfiguration
            '''
            result = self._values.get("destination_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty"]], result)

        @builtins.property
        def scope(self) -> typing.Optional[builtins.str]:
            '''The organizational scope to which the rule applies, specified using accounts or organizational units.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-scope
            '''
            result = self._values.get("scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selection_criteria(self) -> typing.Optional[builtins.str]:
            '''Criteria for selecting which resources the rule applies to, such as resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-selectioncriteria
            '''
            result = self._values.get("selection_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_format": "logFormat",
            "max_aggregation_interval": "maxAggregationInterval",
            "traffic_type": "trafficType",
        },
    )
    class VPCFlowLogParametersProperty:
        def __init__(
            self,
            *,
            log_format: typing.Optional[builtins.str] = None,
            max_aggregation_interval: typing.Optional[jsii.Number] = None,
            traffic_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration parameters specific to VPC Flow Logs.

            :param log_format: The format in which VPC Flow Log entries should be logged.
            :param max_aggregation_interval: The maximum interval in seconds between the capture of flow log records.
            :param traffic_type: The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                v_pCFlow_log_parameters_property = observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                    log_format="logFormat",
                    max_aggregation_interval=123,
                    traffic_type="trafficType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__945b01222f6573dfd9bd365335b34de4d056db844b2fe9ffa6c9d40371eaff6e)
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
                check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_format is not None:
                self._values["log_format"] = log_format
            if max_aggregation_interval is not None:
                self._values["max_aggregation_interval"] = max_aggregation_interval
            if traffic_type is not None:
                self._values["traffic_type"] = traffic_type

        @builtins.property
        def log_format(self) -> typing.Optional[builtins.str]:
            '''The format in which VPC Flow Log entries should be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-logformat
            '''
            result = self._values.get("log_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
            '''The maximum interval in seconds between the capture of flow log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-maxaggregationinterval
            '''
            result = self._values.get("max_aggregation_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_type(self) -> typing.Optional[builtins.str]:
            '''The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-traffictype
            '''
            result = self._values.get("traffic_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCFlowLogParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, ITelemetryRuleRef, _ITaggableV2_4e6798f8)
class CfnTelemetryRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule",
):
    '''Creates a telemetry rule that defines how telemetry should be configured for AWS resources in your account.

    The rule specifies which resources should have telemetry enabled and how that telemetry data should be collected based on resource type, telemetry type, and selection criteria.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::TelemetryRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_telemetry_rule = observabilityadmin.CfnTelemetryRule(self, "MyCfnTelemetryRule",
            rule=observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                resource_type="resourceType",
                telemetry_type="telemetryType",
        
                # the properties below are optional
                destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                ),
                selection_criteria="selectionCriteria"
            ),
            rule_name="ruleName",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: Retrieves the details of a specific telemetry rule in your account.
        :param rule_name: The name of the telemetry rule.
        :param tags: Lists all tags attached to the specified telemetry rule resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb28d06ef60815f8488b771b64aca8e3671a315a3f6676ad80a414dcd296224)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTelemetryRuleProps(rule=rule, rule_name=rule_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c971c1c4e8e03d4140674a22f18490c0a14f143dab5c9b15a801d0e69e908b92)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adf48e055c256d6f5cb987ba3921807e211a303c3d38be6a02b6932f52a739fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the telemetry rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="telemetryRuleRef")
    def telemetry_rule_ref(self) -> TelemetryRuleReference:
        '''A reference to a TelemetryRule resource.'''
        return typing.cast(TelemetryRuleReference, jsii.get(self, "telemetryRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"]:
        '''Retrieves the details of a specific telemetry rule in your account.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253115d76ca17e48e13df2aa679666bb12581680b457a45a7743f6a80d6dbfa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the telemetry rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59aae5f9c690d805a52b4e5949569db025239eb21172f781673428651a87d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Lists all tags attached to the specified telemetry rule resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4f4991901119d1b8ec2bf2b1d23daff9627e5f20b555f27ec8fd5bc58890b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_pattern": "destinationPattern",
            "destination_type": "destinationType",
            "retention_in_days": "retentionInDays",
            "vpc_flow_log_parameters": "vpcFlowLogParameters",
        },
    )
    class TelemetryDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            destination_pattern: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
            retention_in_days: typing.Optional[jsii.Number] = None,
            vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.VPCFlowLogParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying where and how telemetry data should be delivered for AWS resources.

            :param destination_pattern: The pattern used to generate the destination path or name, supporting macros like and .
            :param destination_type: The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").
            :param retention_in_days: The number of days to retain the telemetry data in the destination.
            :param vpc_flow_log_parameters: Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_destination_configuration_property = observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01ec7a824466c4f6343ec939656046b6c12a168edd9bbf6ebca41e4b5d1554d5)
                check_type(argname="argument destination_pattern", value=destination_pattern, expected_type=type_hints["destination_pattern"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
                check_type(argname="argument vpc_flow_log_parameters", value=vpc_flow_log_parameters, expected_type=type_hints["vpc_flow_log_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_pattern is not None:
                self._values["destination_pattern"] = destination_pattern
            if destination_type is not None:
                self._values["destination_type"] = destination_type
            if retention_in_days is not None:
                self._values["retention_in_days"] = retention_in_days
            if vpc_flow_log_parameters is not None:
                self._values["vpc_flow_log_parameters"] = vpc_flow_log_parameters

        @builtins.property
        def destination_pattern(self) -> typing.Optional[builtins.str]:
            '''The pattern used to generate the destination path or name, supporting macros like  and .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationpattern
            '''
            result = self._values.get("destination_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retention_in_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain the telemetry data in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-retentionindays
            '''
            result = self._values.get("retention_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_flow_log_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.VPCFlowLogParametersProperty"]]:
            '''Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters
            '''
            result = self._values.get("vpc_flow_log_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.VPCFlowLogParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "telemetry_type": "telemetryType",
            "destination_configuration": "destinationConfiguration",
            "selection_criteria": "selectionCriteria",
        },
    )
    class TelemetryRuleProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            telemetry_type: builtins.str,
            destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.TelemetryDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            selection_criteria: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines how telemetry should be configured for specific AWS resources.

            :param resource_type: The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC").
            :param telemetry_type: The type of telemetry to collect (Logs, Metrics, or Traces).
            :param destination_configuration: Configuration specifying where and how the telemetry data should be delivered.
            :param selection_criteria: Criteria for selecting which resources the rule applies to, such as resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_rule_property = observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
                
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    selection_criteria="selectionCriteria"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25d1c19a045d927560ccf78552c0595fbd7db1322a4e66f60e4d9cb5393b81c3)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument telemetry_type", value=telemetry_type, expected_type=type_hints["telemetry_type"])
                check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
                check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_type": resource_type,
                "telemetry_type": telemetry_type,
            }
            if destination_configuration is not None:
                self._values["destination_configuration"] = destination_configuration
            if selection_criteria is not None:
                self._values["selection_criteria"] = selection_criteria

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def telemetry_type(self) -> builtins.str:
            '''The type of telemetry to collect (Logs, Metrics, or Traces).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-telemetrytype
            '''
            result = self._values.get("telemetry_type")
            assert result is not None, "Required property 'telemetry_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryDestinationConfigurationProperty"]]:
            '''Configuration specifying where and how the telemetry data should be delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-destinationconfiguration
            '''
            result = self._values.get("destination_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryDestinationConfigurationProperty"]], result)

        @builtins.property
        def selection_criteria(self) -> typing.Optional[builtins.str]:
            '''Criteria for selecting which resources the rule applies to, such as resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-selectioncriteria
            '''
            result = self._values.get("selection_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_format": "logFormat",
            "max_aggregation_interval": "maxAggregationInterval",
            "traffic_type": "trafficType",
        },
    )
    class VPCFlowLogParametersProperty:
        def __init__(
            self,
            *,
            log_format: typing.Optional[builtins.str] = None,
            max_aggregation_interval: typing.Optional[jsii.Number] = None,
            traffic_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration parameters specific to VPC Flow Logs.

            :param log_format: The format in which VPC Flow Log entries should be logged.
            :param max_aggregation_interval: The maximum interval in seconds between the capture of flow log records.
            :param traffic_type: The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                v_pCFlow_log_parameters_property = observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                    log_format="logFormat",
                    max_aggregation_interval=123,
                    traffic_type="trafficType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb426e63d8ddff6bc9e58865c89c023dbf7b61ef2e21b2f9ff902df9db830681)
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
                check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_format is not None:
                self._values["log_format"] = log_format
            if max_aggregation_interval is not None:
                self._values["max_aggregation_interval"] = max_aggregation_interval
            if traffic_type is not None:
                self._values["traffic_type"] = traffic_type

        @builtins.property
        def log_format(self) -> typing.Optional[builtins.str]:
            '''The format in which VPC Flow Log entries should be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-logformat
            '''
            result = self._values.get("log_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
            '''The maximum interval in seconds between the capture of flow log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-maxaggregationinterval
            '''
            result = self._values.get("max_aggregation_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_type(self) -> typing.Optional[builtins.str]:
            '''The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-traffictype
            '''
            result = self._values.get("traffic_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCFlowLogParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


__all__ = [
    "CfnOrganizationCentralizationRule",
    "CfnOrganizationCentralizationRuleProps",
    "CfnOrganizationTelemetryRule",
    "CfnOrganizationTelemetryRuleProps",
    "CfnTelemetryRule",
    "CfnTelemetryRuleProps",
    "IOrganizationCentralizationRuleRef",
    "IOrganizationTelemetryRuleRef",
    "ITelemetryRuleRef",
    "OrganizationCentralizationRuleReference",
    "OrganizationTelemetryRuleReference",
    "TelemetryRuleReference",
]

publication.publish()

def _typecheckingstub__00d0ecee2cd9ac728ca3e321203ce2e611e56b0b2d415ba2673a50599e4512cd(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c94381428dd096d5bd5b31c1a78b0ec6c66b125c46a889f389e957dbf9f76b(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7455cb845b044ed569a8ec8407abf811920062f00d1e54ad191e90dc9b7e2811(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b3ad11b09d25a384211da640f6a09bc1e0c17db4ccd5b1f32b27309ce4215f5(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__546326e4a1c8218daecae9d95475d22bf60d95f4d5ec20cd304d51ba67eb92f4(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5c59e1cd03c9d8825ebf008d30354018de9d95b37c45267b93575de094bcfc(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18acbc8917f3c4cbc8bb06f5fae76010e41ab5f0e9b157f4c324c214a180ef2e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b2ea8ec552fc96b3662b368fa64eea5f82839c3bd0f1aa52bd64bc495f5341(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f130448a4f76aff49b8e31a382ea5ab14eacdf34a74afe86be23352ded6622e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fbb5a84b6997cee28db4665d22fee83629861a1e51fe754b85b3858441e7c2d(
    value: typing.Union[_IResolvable_da3f097b, CfnOrganizationCentralizationRule.CentralizationRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42b1edd10be1da3c565db5f9585850487a7c51b5ad7ab0a72c1d4345b4ac7f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58679a9a3a800195cc0ecf82553695580c2dd2061901e27320b9025cb6ed262(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48736d0ec2563919af9b82675cbe965d2288bd15210b9c8b34911e7a89ae0f47(
    *,
    region: builtins.str,
    account: typing.Optional[builtins.str] = None,
    destination_logs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb475427ce4a2316b8478f1c58d17ddd5783412b26cdfb98819c47313aa718dc(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4d1dff0252b97263e138c77bea2f698277762eeffd4fcf3911e496ac5762e4(
    *,
    regions: typing.Sequence[builtins.str],
    scope: typing.Optional[builtins.str] = None,
    source_logs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd7a39f2c94fa5f25cdcfc83cd888a8c3b22c09afa009f3ed5de76fd5befe41(
    *,
    backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    logs_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d26acca25f06381fb096b21a6f3791d0ef735549ac7bae5795f4e646184d86(
    *,
    region: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d66f88a29d04606b9d6748d2a92fb0d7bf4a500a64fceff8556e1ac2275828e(
    *,
    encryption_strategy: builtins.str,
    encryption_conflict_resolution_strategy: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a12247cb1287e19ec3a764cc738d756d26c889450a5b771811f8378a2b5d6c(
    *,
    encrypted_log_group_strategy: builtins.str,
    log_group_selection_criteria: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a67d6a9dd82924a413b7d3435faeb8efa735048df0244b926e672def8c2d5f75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb893813673a29ee1f384593916d34bdcc440b816dfc54ad27097692c5a64e9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c809c768027da00df4018694393faf5d77af9754b12923bf684ada119faecfc7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97cf84910a3c46b94c3e90ddf73c07b304a029e413bebd1b7c5e7b2bbe5cd411(
    value: typing.Union[_IResolvable_da3f097b, CfnOrganizationTelemetryRule.TelemetryRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84099afcf940dd46614099ecc03e181396a6d202813d1517bd79414c5aa2f5ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d494e45ec3f03fbc2168c2e374f689615e98524c832aa6247ad243fabe01ffe7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b4168c57b4555036ca598e8299a36985c9aab7a1eb6b84357df4454b340171(
    *,
    destination_pattern: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8febf24ebcbc00029972152d874df5e847a9f5cd45e05abb26e69f7a2cabc5bf(
    *,
    resource_type: builtins.str,
    telemetry_type: builtins.str,
    destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scope: typing.Optional[builtins.str] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945b01222f6573dfd9bd365335b34de4d056db844b2fe9ffa6c9d40371eaff6e(
    *,
    log_format: typing.Optional[builtins.str] = None,
    max_aggregation_interval: typing.Optional[jsii.Number] = None,
    traffic_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb28d06ef60815f8488b771b64aca8e3671a315a3f6676ad80a414dcd296224(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c971c1c4e8e03d4140674a22f18490c0a14f143dab5c9b15a801d0e69e908b92(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf48e055c256d6f5cb987ba3921807e211a303c3d38be6a02b6932f52a739fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253115d76ca17e48e13df2aa679666bb12581680b457a45a7743f6a80d6dbfa1(
    value: typing.Union[_IResolvable_da3f097b, CfnTelemetryRule.TelemetryRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59aae5f9c690d805a52b4e5949569db025239eb21172f781673428651a87d80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4f4991901119d1b8ec2bf2b1d23daff9627e5f20b555f27ec8fd5bc58890b7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ec7a824466c4f6343ec939656046b6c12a168edd9bbf6ebca41e4b5d1554d5(
    *,
    destination_pattern: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.VPCFlowLogParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d1c19a045d927560ccf78552c0595fbd7db1322a4e66f60e4d9cb5393b81c3(
    *,
    resource_type: builtins.str,
    telemetry_type: builtins.str,
    destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb426e63d8ddff6bc9e58865c89c023dbf7b61ef2e21b2f9ff902df9db830681(
    *,
    log_format: typing.Optional[builtins.str] = None,
    max_aggregation_interval: typing.Optional[jsii.Number] = None,
    traffic_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IOrganizationCentralizationRuleRef, IOrganizationTelemetryRuleRef, ITelemetryRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
