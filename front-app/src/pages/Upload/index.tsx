import { useForm } from 'react-hook-form'
import './index.css'

interface InputFile {
    picture: FileList
}

const Page = () => {
    const { register, handleSubmit } = useForm()

    const toBase64 = (file: any) => new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    })

    const onSubmitForm = async (data: InputFile) => {
        const file = data.picture.item(0)

        console.log("=====")
        console.log(file)
        console.log("=====")
        console.log(await toBase64(file))
        console.log("=====")
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
