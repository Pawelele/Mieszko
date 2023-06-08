import logo from './logo.svg';
import './App.css';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import RootLayout from './layouts/RootLayout';
import MainView from './views/MainView';
import SearchView from './views/SearchView';
import AboutUs from './views/AboutUs/AboutUs';
import TermsAndConditions from './views/TermsAndConditions/TermsAndConditions';
import Contact from './views/Contact/Contact';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    children: [
      { path: '/', element: <MainView /> },
      { path: '/mieszkania', element: <SearchView /> },
      { path: '/onas', element: <AboutUs /> },
      { path: '/regulamin', element: <TermsAndConditions /> },
      { path: '/kontakt', element: <Contact /> },
    ]
  }
])

function App() {
  return (
    <RouterProvider router={router}></RouterProvider>
  );
}

export default App;
