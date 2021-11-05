import { useState, useEffect } from 'react'

const API_GATEWAY = 'https://vemb2pohx7.execute-api.us-east-1.amazonaws.com/prod'


const Page = () => {
    const [ data, setData ] = useState({
        message: String,
        images: []        
    })
    const [ isLoading, setIsLoading ] = useState(true)
    const [ error, setError ] = useState(null)

    useEffect(() => {
        fetch(`${API_GATEWAY}/images`)
            .then(res => res.json())
            .then(data => setData(data))
            .catch(err => setError(err))
            .finally(() => setIsLoading(!isLoading))
    }, [])

    if (isLoading) {
        return null
    }

    if (error) {
        return (
            <div>
                <p>An error occurs...</p>
            </div>
        )
    }

    const { images } = data

    return (
        <div>
            <h1>Files List Page</h1>
            {
                images.map(image => <img key={image} src={image} alt='' />)
            }
        </div>
    )
}

export default Page
