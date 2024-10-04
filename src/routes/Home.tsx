import { useState } from 'react';

import Card from '@/components/Card';
import Page from '@/components/Page';
import { Input } from '@/components/ui/input';
import {
  Button,
  Text,
  VStack,
} from '@chakra-ui/react';

export default function Home(){
  const [file, setFile] = useState(null);
  const [spreadsheet, setSpreadsheet] = useState(null);

  const handleFileSelected = (e: any) => {
    const file = e.target.files[0];
    setFile(file);
  }

  const handleSubmitSpreadsheet = (e: any) => {
    setSpreadsheet(file)
    e.currentTarget.disabled = true;
  }

  return(
    <Page>
      <Card heading="Sync with B3" subtitle="Please upload your B3 spreadsheet" topElements={[]}>
        <VStack className="flex-1" alignItems="flex-start">
          <Text size="sm"><label htmlFor="b3-spreasheet">{spreadsheet === null ? "No file selected" : "File selected"}</label></Text>
          <Input disabled={spreadsheet === null ? false : true} className="rounded-xl" id="b3-spreadsheet" type="file" accept=".xlsx" onChange={handleFileSelected}/>
          <Button isLoading={spreadsheet !== null} variant='outline' marginLeft="auto" marginRight="auto" onClick={handleSubmitSpreadsheet}>
            Submit
          </Button>
        </VStack>
      </Card>
    </Page>
  )
}