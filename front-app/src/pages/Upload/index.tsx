import { useForm } from 'react-hook-form'
import './index.css'

interface InputFile {
    picture: FileList
}

const API_GATEWAY = 'https://i7mka11fei.execute-api.us-east-1.amazonaws.com/prod'

const Page = () => {
    const { register, handleSubmit } = useForm()

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

        console.log('=====')
        console.log(body)
        console.log('=====')

        fetch(`${API_GATEWAY}/images`, {
            method: 'POST',
            body: JSON.stringify(body)
        })
            .then(() => console.log('====='))
            .catch(() => console.log('oh no :('))

    }

    return (
        <div className='fa-upload-page'>
            <h1>Upload File Page</h1>
            <form onSubmit={handleSubmit(onSubmitForm)} action="#" method="POST">
                <input {...register('picture')} type="file" name='picture' />
                <button type='submit'>Upload</button>
            </form>
        </div>
    )
}

export default Page
