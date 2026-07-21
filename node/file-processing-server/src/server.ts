import { app } from "./app";
import "./listeners/job.listener";

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`server running on ${PORT}`);
});
