import { Box, Button } from "@chakra-ui/react"

function Card({name, price}){
    return (
        <Box maxW="sm" borderWidth="1px" borderRadius="lg" overflow="hidden">
            <Box p="6">
                <Box
                  mt="1"
                  fontWeight="semibold"
                  as="h4"
                  lineHeight="tight"
                  isTruncated
                >
                    {name}
                </Box>
                <Box>{price} €</Box>
                <Box marginTop={8}>
                    <Button colorScheme="teal" size="sm">Show more info</Button>
                </Box>
            </Box>
        </Box>
    )
}

export default Card