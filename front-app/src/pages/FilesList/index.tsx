import { useState, useEffect } from 'react'

import { API_GATEWAY } from '../../constants'
import './index.css'

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

    const renderPageContent = () => {
        if (isLoading) {
            return (<p>Loading...</p>)
        }

        if (error) {
            return <p>An error occurs...</p>
        }

        const { images } = data
        return images.length ?
            images.map(image => <img key={image} src={`https://${image}`} alt='' className='fa-files-list-image' />)
            : <p>No images</p>
    }

    return (
        <div className='fa-files-list'>
            <h1 className='title fa-files-list-title'>Your Uploaded Images</h1>
            <div className='fa-files-list-content'>
                {
                    renderPageContent()
                }
            </div>
        </div>
    )
}

export default Page
