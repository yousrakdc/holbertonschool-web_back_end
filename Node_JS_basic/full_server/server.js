import { Express } from "express";
import { routes } from "./routes/index.js";

const app = express();
const port = 1245;

const [,, database] = process.argv;
app.set('databasePath', database);

app.use('/', routes);

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});

export default app;