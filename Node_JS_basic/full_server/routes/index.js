import { Express } from "express";
import AppController from "../controllers/AppController";
import StudentsController from "../controllers/StudentsController";
import { get } from "../../6-http_express";

const router = express.Router();

router;get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;