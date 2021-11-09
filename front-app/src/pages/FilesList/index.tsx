import { useState, useEffect } from 'react'

import { API_GATEWAY } from '../../constants'


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
            <h1 className='title'>Files List Page</h1>
            {
                images.length ?
                    images.map(image => <img key={image} src={image} alt='' />)
                    : <p>No images</p>
            }
        </div>
    )
}

export default Page
