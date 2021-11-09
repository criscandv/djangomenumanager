import { useEffect, useState } from "react";
import { getMenus } from "./api/menu";

import { Grid, Box, FormControl, FormLabel, Input, Heading } from "@chakra-ui/react"
import Card from './components/Card'

function App() {
    const [menus, setMenus] = useState([])
    useEffect(() => {
        getMenusData()
    }, [])

    const getMenusData = (name="") => {
        getMenus(name).then(response => {
            let { data } = response
            setMenus(data)
        });
    }

    const handleChange = event => {
        let name = event.target.value;
        getMenusData(name)
    }

    return (
        <Box w="80%" margin="auto" marginTop="10">
            <Heading textAlign="center" as="h1" size="2xl">
                Menu manager
            </Heading>
            <FormControl id="email" marginBottom="30">
                <FormLabel>Find by name</FormLabel>
                <Input type="text" placeholder="Menu name" onChange={handleChange}/>
            </FormControl>
            <Heading as="h3" size="lg">
                Menu list
            </Heading>
            {
            menus.length && <Grid templateColumns="repeat(5, 1fr)" gap={6}>
                {menus.map(menu => (
                    <Card key={menu.id} name={menu.name} price={menu.price}/>
                ))}
            </Grid>
            }
        </Box>
    );
}

export default App;
