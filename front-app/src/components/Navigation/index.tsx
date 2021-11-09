import { Link } from "react-router-dom"

import './index.css'

const Component = () => (
    <nav className='main-nav'>
        <ul>
            <li className='nav-item'>
                <Link to="/" className='nav-link'>
                    Home
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/upload" className='nav-link'>
                    Upload image
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/files-list" className='nav-link'>
                    Files List
                </Link>
            </li>
        </ul>
    </nav>
)

export default Component
