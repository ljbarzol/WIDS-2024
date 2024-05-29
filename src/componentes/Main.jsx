const Main = () => {
    return (
        <div className="border">
            <div className="flex flex-col h-screen justify-center items-center">
                <div> 
                    <p className="cursor-pointer">Slogan</p>
                </div>
                <div> 
                    <button>Boton</button>
                </div>
            </div>
            <div className="flex">
                <input type="text"/>
                <input type="text"/>
                <input type="text"/>
            </div>
        </div>
    );
}
export default Main;
