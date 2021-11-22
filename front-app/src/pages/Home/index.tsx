import './index.css'

const Page = () => (
    <div className='fa-homepage'>
        <h1 className='title fa-homepage-title'>Serverless Image Uploader</h1>
        <small>Upload and share your images</small>
        <div className='fa-homepage-img-wrapper'>
            <img className='fa-homepage-img' src="/screenshot.png" alt="An example result of uploaded images" />
        </div>
    </div>
)

export default Page
