import './index.css';

import { StrictMode } from 'react';

import { createRoot } from 'react-dom/client';
import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router-dom';

import { ChakraProvider } from '@chakra-ui/react';

import Home from './routes/Home';
import Root from './routes/root';
import theme from './theme';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
  },
  {
    path:"/home",
    element: <Home/>,
  }
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ChakraProvider theme={theme}>
    <RouterProvider router={router}/>
    </ChakraProvider>
  </StrictMode>,
)
