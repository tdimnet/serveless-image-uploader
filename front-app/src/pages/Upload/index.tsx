import { useState } from 'react'
import { useForm } from 'react-hook-form'

import './index.css'

const API_GATEWAY = 'https://vemb2pohx7.execute-api.us-east-1.amazonaws.com/prod'

const Page = () => {
    const { register, handleSubmit } = useForm()
    const [ image, setImage ] = useState(null)

    const toBase64 = (file: any) => new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    })

    const onSubmitForm = async (data: any) => {
        const file = data.picture.item(0)
        const fileBase64 = await toBase64(file)

        const body = {
            name: file.name,
            file: fileBase64
        }


        fetch(`${API_GATEWAY}/images`, {
            method: 'POST',
            body: JSON.stringify(body)
        })
            .then(res => res.json())
            .then(data => setImage(data.image_path))
            .catch(() => console.log('oh no :('))

    }

    return (
        <div className='fa-upload-page'>
            <h1>Upload File Page</h1>
            <form onSubmit={handleSubmit(onSubmitForm)} action="#" method="POST">
                <input {...register('picture')} type="file" name='picture' required />
                <button type='submit'>Upload</button>
            </form>
            {
                image && <img className='fa-uploaded-img' src={image} alt='' />
            }
        </div>
    )
}

export default Page
