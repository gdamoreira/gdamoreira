# Hi, I'm Guilherme

### Staff / Senior Software Engineer | Distributed Systems Architecture & Application Security

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=339933&center=true&vCenter=true&width=800&lines=Staff+%2F+Senior+Software+Engineer;15%2B+years+designing+distributed+backend+platforms;Kotlin+%7C+Java+%7C+Quarkus+%7C+Spring+Boot+%7C+Kafka;Event-driven+architecture+%7C+CQRS+%7C+gRPC;Application+Security+%26+DevSecOps;Creator+of+Snodra)](https://readme-typing-svg.demolab.com)

[![Open to Staff, Tech Lead and Architect roles](https://img.shields.io/badge/Open_to-Staff_%7C_Tech_Lead_%7C_Architect_roles-brightgreen?style=for-the-badge)](https://www.linkedin.com/in/gdamoreira)

Senior software engineer and technical leader based in Barcelona, open to remote. For 15+ years I have designed, scaled and secured distributed backend platforms across PropTech, cybersecurity, FinTech and enterprise SaaS, owning the architecture end to end.

My home ground is event-driven systems on the JVM: Kotlin and Java, Quarkus and Spring Boot, Apache Kafka and PostgreSQL, running on AWS and Kubernetes. I also spent more than three years as an application security engineer at Oracle, so threat modeling, static analysis and a secure SDLC are part of how I design systems, not a review at the end.

---

## Career highlights

- **A US$100 million exit.** Tech lead on the 3D production platform that took Decora from about 15 people to over 150 and to its acquisition by CreativeDrive, the second-largest Brazilian tech deal of 2018.
- **Real-time platform architecture.** At Beyonnex I architected and led the IoT ingestion and calculation pipelines that turn continuous meter telemetry into heating consumption and billing for German real estate portfolios, replacing manual batch processes.
- **Security built into engineering.** At Oracle (NetSuite) I architected the internal static analysis and code-auditing tools that sped up vulnerability detection across large enterprise codebases, and mentored engineering teams on secure design.
- **Platform ownership in cybersecurity.** Led end-to-end architecture and delivery of Phoenix Security's enterprise ASPM platform.
- **Executive experience.** CTO of Reticomm for two years: engineering strategy, cloud infrastructure and product delivery.
- **Credentials.** Postgraduate degree in Data Science Engineering, MBA in Project Management, and three Black Hat certifications in API security, security automation and malware analysis.

---

## Featured project: Snodra

**[Snodra](https://snodra.damoreira.com)** is an open-source messaging stack for services that speak events and gRPC. It gives a service fleet commands, queries, events and sagas over the gRPC and Kafka it already runs, with no broker in the request path, no proprietary event store and no per-node licence. I design and maintain the whole project, from the wire protocol to the documentation.

| Repository | What it is | Language |
|---|---|---|
| [snodra-server](https://github.com/snodra/snodra-server) | Stateless gRPC router and control plane. It stores nothing and queues nothing, so every instance is independent. | Rust |
| [snodra-messaging](https://github.com/snodra/snodra-messaging) | Client library with a Spring Boot starter, published to Maven Central | Kotlin |
| [snodra-messaging-rs](https://github.com/snodra/snodra-messaging-rs) | Client library, published to crates.io | Rust |
| [snodra-messaging-go](https://github.com/snodra/snodra-messaging-go) | Client library | Go |
| [snodra-conformance](https://github.com/snodra/snodra-conformance) | Conformance suite that checks every client against a real server, so the protocol is the stable contract | Rust |
| [snodra-event-browser](https://github.com/snodra/snodra-event-browser) | Read-only event browser add-on for the dashboard | Rust |

Events go through a transactional outbox, in the same database transaction as the state they describe. Stores are pluggable (Kafka or RabbitMQ Streams for events; PostgreSQL, MySQL or MongoDB for messages), and security covers static tokens, OAuth2/OIDC JWT and mTLS with per-service ACLs. Pre-1.0, Apache-2.0.

[![Snodra site](https://img.shields.io/badge/snodra.damoreira.com-1a1033?style=for-the-badge&logo=googlechrome&logoColor=white)](https://snodra.damoreira.com) [![Snodra on GitHub](https://img.shields.io/badge/github.com%2Fsnodra-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/snodra)

---

## Tech Stack

### Backend

[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) [![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white) [![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white) [![Quarkus](https://img.shields.io/badge/Quarkus-4695EB?style=for-the-badge&logo=quarkus&logoColor=white)](https://img.shields.io/badge/Quarkus-4695EB?style=for-the-badge&logo=quarkus&logoColor=white) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) [![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)

### Messaging & Architecture

[![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white) [![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white) [![REST APIs](https://img.shields.io/badge/REST_APIs-005571?style=for-the-badge&logo=openapiinitiative&logoColor=white)](https://img.shields.io/badge/REST_APIs-005571?style=for-the-badge&logo=openapiinitiative&logoColor=white) [![gRPC](https://img.shields.io/badge/gRPC-244C5A?style=for-the-badge&logo=grpc&logoColor=white)](https://img.shields.io/badge/gRPC-244C5A?style=for-the-badge&logo=grpc&logoColor=white) [![CQRS](https://img.shields.io/badge/CQRS_%26_Event--Driven-4E4B66?style=for-the-badge)](https://img.shields.io/badge/CQRS_%26_Event--Driven-4E4B66?style=for-the-badge)

### Cloud & DevOps

[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) [![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) [![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white)](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white) [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white) [![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) [![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white) [![Gradle](https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white)](https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white) [![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white) [![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### Databases

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) [![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) [![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white) [![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white) [![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)

### Frontend

[![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white) [![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) [![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D) [![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white) [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Testing & Security

[![JUnit5](https://img.shields.io/badge/JUnit5-25A162?style=for-the-badge&logo=junit5&logoColor=white)](https://img.shields.io/badge/JUnit5-25A162?style=for-the-badge&logo=junit5&logoColor=white) [![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white) [![Application Security](https://img.shields.io/badge/Application_Security-4E4B66?style=for-the-badge)](https://img.shields.io/badge/Application_Security-4E4B66?style=for-the-badge)

---

## What I do

- **Architecture**: distributed systems, microservices, event-driven architecture (CQRS), Domain-Driven Design and REST/gRPC APIs, designed for high availability
- **Backend platforms**: Kotlin, Java, Quarkus and Spring Boot services with Apache Kafka and PostgreSQL
- **Cloud & delivery**: AWS, Docker, Kubernetes and Terraform, with CI/CD from commit to production
- **Application security**: ASPM, SAST/DAST automation, threat modeling, API security and a secure SDLC
- **Technical leadership**: technical strategy, cross-team architecture alignment, engineering standards and mentoring

---

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=gdamoreira&show_icons=true&theme=dark&hide_border=true)](https://github.com/gdamoreira) [![GitHub Streak](https://streak-stats.demolab.com?user=gdamoreira&theme=dark&hide_border=true)](https://github.com/gdamoreira) [![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=gdamoreira&layout=compact&theme=dark&hide_border=true)](https://github.com/gdamoreira)

---

## Get in touch

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gdamoreira) [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guilherme@damoreira.com) [![Website](https://img.shields.io/badge/damoreira.com-000000?style=for-the-badge&logo=googlechrome&logoColor=white)](https://damoreira.com)

---

## Beyond code

When I am not coding you will find me practicing karate, at the gym, gaming, reading, studying new technologies or tinkering with my home lab.

[![Visitor Count](https://komarev.com/ghpvc/?username=gdamoreira&color=blueviolet&style=flat)](https://github.com/gdamoreira)
