import base64
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyCuImlZkx-AbYoSrONVvfAr-vATsrQWnZE"))

def gemini_response(input,pdf_content,prompt): 
    model=genai.GenerativeModel("gemini-1.5-pro")
    response=model.generate_content( [input,pdf_content[0],prompt] )
    return response.text

def gemini_res(input,prompt):
    model=genai.GenerativeModel("gemini-1.5-pro") 
    response= model.generate_content([input,prompt] )  
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images=pdf2image.convert_from_bytes(uploaded_file.read()) #converting PDF to Image
        first_page=images[0]
    
        bytearray=io.BytesIO()
        first_page.save(bytearray,format="JPEG")
        bytearray=bytearray.getvalue()

        pdf_parts = [
                {
                'mime_type':'image/jpeg',
                'data':base64.b64encode(bytearray).decode()
                }
            ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("About the Resume")

submit2 = st.button("What can I do to improvise my skills")

submit3 = st.button("Percentage match")
submit4 = st.button("tailer resume")
submit5= st.button("Generate resume")


input_prompt1= ''' As an HR expert with experience in one of the following roles: Data Scientist, Web Developer, Big Data Engineer, or Data Analyst,
please evaluate the provided resume against the given job description. Assess how well the candidate’s qualifications match the job requirements,
and provide a detailed evaluation highlighting their strengths and weaknesses relative to the role.'''

# input_prompt1 ='''You are an expert you are an experienced HR with tech experience in the field of any one job role in either data science 
# or web development or big data engineering or data analyst, your task is to review the Provide against the job description
# for all these profiles. Please share your professional evaluation on whether the candidate profile aligns with the role. 
# Highlight the strength and weakness of the applicant in relation to the specified job requirements '''


input_prompt2 = '''As a technical HR manager with expertise in one of the following roles: Data Scientist, Web Developer, Big Data Engineer, or Data Analyst,
review the provided resume in the context of the given job description. Offer insights on the candidate’s skills and qualifications from an HR perspective,
and provide recommendations for skill enhancement and areas for improvement to better align with the job requirements.'''



# input_prompt2 = ''' You are a technical human resource manager with expertise in field of any one job role in either data science 
# or web development or big data engineering or data analyst, your role is to scrutinize the résumé in light of the job 
# description provided. Share your insights on the candidates' skills for the role from HR perspective. 
# Additionally offer advice on enhancing the candidate skills and identify areas of improvement. '''


input_prompt3 = '''As an ATS expert with in-depth knowledge of the following roles: Data Scientist, Web Developer, Big Data Engineer, or Data Analyst,
evaluate the provided resume against the job description. Provide a percentage score indicating how well the resume matches the job description,
followed by a list of missing keywords and any final thoughts or observations along with a match percentage of resume to job description.'''





# input_prompt3 = ''' You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding field of any one 
# job role in either data science or web development or big data engineering or data analyst, and deep ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume 
# matches the job description. First the output should come as percentage and then keywords missing and last final thoughts. '''

input_prompt4= '''You are a skilled ATS(Appliication Tracking System) comapatable resume writer with deep understanding of devops and generative ai field along with complete ATS functionality, 
Your Task is to tailor the resume according to the job description and give me the resume the output should be as given resume format and it must match up to 95 percent of job description. Also mention below what are the chnages you have made'''

input_prompt5 = '''You are a skillled ATS(Appliication Tracking System) comapatable resume writer with deep understanding of Generative ai field along with complete ATS functionality,
Your task is to generate a resume according to thre job description and given. Consider the below example 
###
job description:

Skilled in Containers / Container Orchestration (Kubernetes, Docker)
Experience with Linux servers either physical, virtual or cloud instances
Understanding of networking concepts
Experience with a cloud provider, Google Cloud Platform preferred but not necessary
Experience using source control, specifically GIT, including knowledge of Bitbucket, GitHub or Gitlab
Experience in the use of Terraform or similar IAC tools
Knowledge of least one development or scripting language (i.e., Python, Java, JavaScript, Go, Ruby, .NET, etc.)
Knowledgeable of CI/CD tools such as Gitlab, Jenkins, TravisCI, etc.
Understanding of microservices
Understanding of Agile software development concepts (for example, Scrum, Kanban)
Ability to decompose complex processes into understandable components/processes
Ability to schedule, estimate, priorities and deliver to commitments with several parallel ongoing efforts
Basic Understanding of Identity and Access Management controls and concepts
Awareness of configuration management tools, preferably Ansible
Ability to work at scale with shifting timelines and priorities.
Proven ability to communicate using oral and written methods
Passion and interest to both continually innovate and adopt industry continuous delivery best practices
Proactive and collaborative team member 
###
resume sample: 
professional summary points :
DevOps SRE:
Collaborated with development teams to enhance overall development productivity. Lead a team of DevOps engineers to support machine learning Ops and software development.
Implemented software development best practices, including version control with Git and continuous integration/continuous deployment (CI/CD) pipelines.
Worked closely with software engineering and product management teams to design, deliver, and manage services with high uptime.
Created frameworks and automation in the development process to maximize build efficiency and ensure secure code.
Highly skilled in building cloud solutions utilizing application services on AWS Managed infrastructure and strategic vendor relationships, including development firms. Developed templates and scripts to automate everyday developer and operations functions.
Used Docker, Kubernetes, and Docker Compose to create clusters of microservices developed in Python .
Conducted performance tuning and optimization initiatives to enhance application speed, scalability, and cost efficiency in cloud environments like AWS Lambda, Azure Functions, 
Led capacity planning efforts to forecast resource needs and optimize infrastructure scalability, leveraging tools like CloudWatch.
 ####
Working experience:

Designed and deployed HIPAA-compliant cloud-native applications using C#.NET and ASP.NET for electronic health records (EHR) systems, ensuring scalability and high availability of patient data.
Led architectural decisions for migrating legacy healthcare systems to the cloud, utilizing AWS CloudFormation and Azure Resource Manager (ARM) templates for consistent, HITRUST CSF-compliant infrastructure provisioning.
Developed microservices for telemedicine platforms using .NET/C# and Web API, employing AWS Lambda for serverless processing of patient data and Azure Kubernetes Service (AKS) for containerized deployments of medical imaging analysis tools.
Implemented dependency injection in ASP.NET MVC framework to enhance modularity and testability of clinical decision support systems.
Established continuous integration pipelines using Jenkins for building and deploying FHIR-compliant healthcare interoperability solutions.
Orchestrated CI/CD processes for medical device software updates, ensuring compliance with FDA regulations for software as a medical device (SaMD).
Automated deployment of J2EE-based clinical trial management systems in an agile environment, adhering to 21 CFR Part 11 requirements for electronic records.
Developed build scripts using ANT and MAVEN in Jenkins for secure, auditable transitions between development, testing, and production environments of healthcare analytics platforms.
Implemented Chef practices and Test Kitchen for developing and testing infrastructure code for HIPAA-compliant cloud environments.
Created RESTful APIs for secure patient data exchange, implementing CRUD operations in compliance with GDPR and CCPA data privacy regulations.
Configured Docker containers for deploying machine learning models for medical image analysis, ensuring reproducibility and scalability.
Utilized Splunk for log analysis and monitoring of clinical systems, providing insights into system performance while maintaining patient data confidentiality.
Employed Ansible for automating the configuration of HIPAA-compliant server environments across healthcare facilities.
Created Dockerfiles for microservices handling sensitive patient information, configuring Tomcat for secure deployment of Java-based healthcare applications.
Managed version control using GitHub and SVN for collaborative development of AI-driven diagnostic tools, maintaining traceability as per regulatory requirements.
Developed PowerShell scripts to automate DICOM data processing tasks and streamline cloud deployments of medical imaging systems.
Utilized ServiceNow for change management and service requests, ensuring compliance with ITIL practices in healthcare IT operations.
Integrated JUnit, FindBugs, and code style analysis tools into the build process for maintaining high code quality in clinical software development.
Leveraged Data Dog and Jira for agile tracking of healthcare software development, enhancing incident management and team collaboration while maintaining audit trails.
Collaborated with cross-functional teams including clinical staff, development, QA, and management to ensure smooth transitions of healthcare IT projects to production, adhering to strict change control procedures.

Environment: Git, SVN, Chef, Jenkins, Docker, Ubuntu, RHEL, .NET/C#, Agile/Scrum, PowerShell, Python, Shell, Spark, ServiceNow, TensorFlow, PyTorch, scikit-learn, FHIR, HL7, DICOM, AWS SageMaker, Azure Machine Learning



Extensive experience in managing high-performance computing environments for large-scale e-commerce data analytics, utilizing RHEL 5/6 and AWS cloud-based solutions to ensure PCI DSS compliance.
Proficient in using AWS OpsWorks (which supports Chef) and AWS Systems Manager for configuration management to automate deployments of recommendation engines and personalization algorithms, ensuring consistent system configurations across the e-commerce platform.
Designed and maintained complex networking setups for distributed e-commerce systems, managing Amazon Route 53 for DNS configurations of multi-region online stores, and ensuring seamless communication through secure protocols, adhering to GDPR and CCPA data protection requirements.
Utilized AWS Key Management Service (KMS) in conjunction with SSH to establish secure remote access for data scientists and analysts, ensuring data confidentiality and integrity in compliance with ISO 27001 standards.
Demonstrated strong analytical skills in diagnosing and resolving complex issues in real-time pricing algorithms and inventory management systems, minimizing downtime and disruptions to the e-commerce platform.
Extensively administered Amazon EC2 instances running Linux for big data processing, utilizing shell scripting and AWS Systems Manager for efficient configuration of Amazon EMR (Elastic MapReduce) clusters used in customer behavior analysis.
Effectively utilized Amazon CloudWatch Logs, AWS X-Ray, and advanced troubleshooting techniques to identify root causes of anomalies in fraud detection models and implement solutions.
Proficient in managing and resolving data science support tickets using AWS Support Center, ensuring timely resolution of issues related to machine learning model deployments and data pipeline failures.
Developed customized monitoring dashboards and alerts using Amazon CloudWatch, enhancing visibility into e-commerce metrics and enabling prompt response to anomalies in conversion rates and customer engagement.
Skillfully maintained diverse operating systems on Amazon EC2 instances supporting various e-commerce analytics tools, ensuring seamless interoperability between different data sources and resolving cross-platform compatibility issues.
Expertise in Amazon EC2 with nested virtualization for creating, managing, and maintaining virtual machines used in A/B testing environments for e-commerce website optimizations.
Implemented and maintained ETL processes using AWS Glue for integrating data from multiple sales channels, ensuring data quality and consistency for downstream machine learning models.
Utilized containerization technologies like Amazon ECS and EKS (Elastic Kubernetes Service) to deploy and scale microservices for product recommendation and dynamic pricing systems.
Implemented data governance frameworks using AWS Lake Formation to ensure compliance with e-commerce regulations, including proper handling of customer data and financial transactions.
Developed and optimized distributed computing workflows using Amazon EMR (Elastic MapReduce) for processing large-scale clickstream data, supporting user behavior analysis and personalized marketing campaigns.
Implemented anomaly detection systems using Amazon SageMaker to identify unusual patterns in order data, supporting fraud prevention efforts and compliance with anti-money laundering regulations.
Utilized natural language processing techniques with Amazon Comprehend to analyze customer reviews and improve product categorization, enhancing search functionality and customer experience.
Implemented and maintained real-time analytics pipelines using Amazon Kinesis for processing streaming e-commerce data, supporting dynamic pricing and inventory management.
Ensured compliance with PSD2 (Payment Services Directive 2) by implementing secure payment processing systems using AWS Key Management Service (KMS) and AWS Certificate Manager for strong customer authentication mechanisms.
Utilized AWS SageMaker for scaling machine learning operations, ensuring compliance with data residency regulations in multinational e-commerce operations.

Environment: RHEL 5/6, AWS OpsWorks, AWS Systems Manager, Docker, Amazon ECS, Amazon EKS, Amazon EMR, Amazon Kinesis, AWS Glue, Python, R, TensorFlow, PyTorch, scikit-learn, NLTK, spaCy, AWS SageMaker, Amazon CloudWatch, AWS X-Ray, AWS Lake Formation, Git, AWS CodePipeline, Amazon Elasticsearch Service, Amazon OpenSearch Service, Amazon RDS for PostgreSQL, Amazon DocumentDB (with MongoDB compatibility), Amazon ElastiCache for Redis.
###

so follow the above instructions and generate a job application ready resume.

'''

if submit1: 
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else: 
        st.write("Please upload the resume")
elif submit2:
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else: 
        st.write("Please upload the resume")
elif submit3: 
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
elif submit4:
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
# elif submit5:
#     if uploaded_file is not None:
#         response=gemini_res(input_prompt5, input_text)
#         st.write(response)
        
    else: 
        st.write("Please upload the resume")

