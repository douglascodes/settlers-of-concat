# Settlers of Concat

## Synopsis
A zero player game to illustrate AWS Step Functions. Using [SFN](https://aws.amazon.com/step-functions/) and [lambda](https://aws.amazon.com/lambda/) Services this is essentially a tutorial. It is based on popular tabletop game mechanics, but that is really just a point of familiarity to make it easier to digest. My work is in research programming, and this came out of a project where we used Step Functions to solve a data audit process requirement. In order to help promote the use of the processes outlined here, we needed a simple framework that could be used as a catalyst for learning methods of the Step Function abbreviated as SFN.
> This tutorial will not explain permissions in IAM, except to say that we use a single role for the StepFunction that has explicit, limited policies for any resources that it needs. These are created and attached to that role as we need them.

## Game Mechanics

Players (CPU) will place datacenters in an emerging marketplace, the hexagonally divided landscape in the new emerging nation of Concat. Depending on the placement of those datacenters, players will gain resources at the beginning of each turn. They can then spend those resources purchasing new datacenters, laying down fiber cable networks or attracting venture capitalists. Once a player reaches 10 VC funders they win the game. Each player starts with two DC locations, worth 1 VC each. Additional DCs must be connected to your existing network.

Resources:
 - Interns
 - Fiber Optic Cables
 - Carbon Tax Credits
 - Ramen Noodles
 - Hard Drives


## Repository 

[https://github.com/douglascodes/settlers-of-concat](https://github.com/douglascodes/settlers-of-concat)


## Requirements 

 - AWS Services Account
 - Python 3.6+
 - Browser
 - Git
 - Text editor
 - Patience
 - Understanding of [AWS IAM](https://aws.amazon.com/iam/)


## Build

There is no "build" since it is a loosely connected set of Lambda functions and other AWS services orchestrated in AWS SFN.


## Tests

TBD


## Reference

 - [AWS Step Functions Tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
 - [AWS Lambda Getting Started](https://aws.amazon.com/lambda/getting-started/)
 - [Input and Output Processing in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html)


## Contributors

[Douglas H. King](https://github.com/douglascodes)


## Version History

### Version 0.2
 - Simplifies the passing of variables with InputPath, OutputPath, ResultPath syntax
 - Adds ChoiceState node to SFN
 - Adds DynamoDB node for Saving game state with PutItem
 - Game loop working.
    1. Save Game State
    2. Roll Die
    3. Advance Turn Number
    4. Choose to continue or End
    5. Repeat until 30 turns

### Version 0.1
 - Lambda function for rolling die.
 - Wrapper Step Function