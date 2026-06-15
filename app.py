from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Docker Application Deployed on AWS ECS</h1>
    <h2>CI/CD using Jenkins, ECR, ECS and ALB</h2>
    <p>Deployment Successful!</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
