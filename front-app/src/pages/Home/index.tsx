import './index.css'

const Page = () => (
    <div className='fa-homepage'>
        <h1 className='title fa-homepage-title'>Serverless Image Uploader</h1>
        <small>Upload and share your images</small>
        <div className='fa-homepage-img-wrapper'>
            <img className='fa-homepage-img' src="/screenshot.png" alt="An example result of uploaded images" />
        </div>
        <ul>
            <li>
                Medium Blog post: <a href="#" target='_blank'>How to create a serverless image uploader with the AWS CDK and React?</a>
            </li>
            <li>
                Datadog Blog post: <a href="#" target='_blank'>How to use Datadog to monitor your serverless infrastructure?</a>
            </li>
        </ul>
    </div>
)

export default Page
