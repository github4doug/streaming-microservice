# Streaming Microservice using AWS Kinesis, AWS Lambda, Redis, Python KCL, and D3.js
[See latest build](http://50.16.95.183/visualize)

## Streaming Microservice
- Clickstream Producer raw events ingested by AWS Kinesis stream
- Python Lambda Consumer processes Kinesis stream and stores cleaned data into Elasticache Redis
- Python webapp prepares realtime visualization response data from in-memory Elasticache Redis
- User views realtime D3.js visualization fed by connection to webapp

<img alt="streaming-microservices" src="https://github4doug.github.io/img/PortfolioDiagram-StreamingMicroservice.png">

# Resources
- [aws samples](https://github.com/aws-samples)
- [snakes-in-the-stream-feeding-and-eating-amazon-kinesis-streams-with-python](https://aws.amazon.com/blogs/big-data/snakes-in-the-stream-feeding-and-eating-amazon-kinesis-streams-with-python/)  