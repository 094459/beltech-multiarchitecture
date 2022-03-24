# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#!/usr/bin/env python3

from aws_cdk import core

from ecs_anywhere.ecs_anywhere_cicd import EcsAnywhereCICDStack
from ecs_anywhere.ecs_anywhere_vpc import EcsAnywhereVPCStack
from ecs_anywhere.ecs_anywhere_pipe import EcsAnywherePipeStack

env_EU=core.Environment(region="eu-central-1", account="704533066374")
props = {
    'awsvpccidr':'10.0.0.0/16',
    'ecsclustername':'beltech-ecs',
    'ecr-repo': 'demo-beltech',
    'code-repo' : 'demo-beltech-repo',
    'image-tag' : 'beltech'
    }

app = core.App()

mydc_vpc = EcsAnywhereVPCStack(
    scope=app,
    id="beltech-anywhere-vpc",
    env=env_EU,
    props=props
)

mydc_ecs_cicd = EcsAnywhereCICDStack(
    scope=app,
    id="beltech-anywhere-ecs",
    env=env_EU,
    vpc=mydc_vpc.vpc,
    props=props  
)

mydc_ecs_pipe = EcsAnywherePipeStack(
    scope=app,
    id="beltech-anywhere-pipe",
    env=env_EU,
    vpc=mydc_vpc.vpc,
    props=props  
)

app.synth()