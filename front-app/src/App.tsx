import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom"

import './global.css'

import HomePage from './pages/Home'
import FilesListPage from './pages/FilesList'
import UploadPage from './pages/Upload'

import Navigation from './components/Navigation'

const App = () => (
    <Router>
        <Navigation />
        <Switch>
            <Route path='/files-list'>
                <FilesListPage />
            </Route>
            <Route path='/upload'>
                <UploadPage />
            </Route>
            <Route path='/'>
                <HomePage />
            </Route>
        </Switch>
    </Router>
)

export default App
