import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function ModalNewSocket(props) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [input, setInput] = React.useState('');
    return (
        <div  >

            <Button  variant="contained"  color="secondary" onClick={handleOpen}>Добавить заметку</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>

                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        Введите новую заметку
                    </Typography>
                    <input value={input} onInput={e => setInput(e.target.value)}/>
                    <Button variant="outlined" onClick={
                        () => {
                            props.handleChange(input)
                        }

                    }>Добавить заметку</Button>

                </Box>

            </Modal>

        </div>

    );

}