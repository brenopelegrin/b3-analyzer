import {
  EmailIcon,
  PhoneIcon,
} from '@chakra-ui/icons';
import {
  Flex,
  Heading,
  HStack,
  IconButton,
  Text,
  useColorModeValue,
  VStack,
} from '@chakra-ui/react';

export default function Card(props: any) {
  const card_bg = useColorModeValue("white", "gray.800");
  const card_border = useColorModeValue("gray.200", "gray.700");

  const exampleIcons = () => {
    return (
      <>
        <IconButton aria-label="Phone" variant='outline' size="md" icon={<PhoneIcon />} />
        <IconButton aria-label="Email" variant='outline' size="md" icon={<EmailIcon />} />
      </>
    )
  }

  return (
    <Flex className="rounded-xl py-4 px-4 border-2" background={card_bg} boxShadow="sm" borderColor={card_border} flexDirection="column">
      <HStack gap="1rem" justifyContent="space-between">
        <VStack alignItems="flex-start" gap="2px">
          <Heading size="md">{props?.heading ? props?.heading : "Default heading"}</Heading>
          <Text fontSize="sm">{props?.subtitle ? props?.subtitle : "Default subtitle"}</Text>
        </VStack>
        <HStack alignItems="flex-end">
          {props?.topElements ? props?.topElements : exampleIcons()}
        </HStack>
      </HStack>

      <Flex className="mt-2 pt-2 border-t-2" borderColor={card_border}>
      {props.children ? props.children : <Text>Default content</Text>}
      </Flex>
    </Flex>
  )
}