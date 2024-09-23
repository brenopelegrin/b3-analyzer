import {
  Container,
  Flex,
} from '@chakra-ui/react';

import Navbar from '../Navbar';

export default function DefaultPage({children}: any) {
  return(
    <Flex direction="column">
      <Navbar/>
      <Container className="mt-2">
        {children}
      </Container>
    </Flex>
  )
}