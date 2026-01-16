import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 10 }, // arranque suave
    { duration: "1m", target: 50 }, // carga media
    { duration: "1m", target: 100 }, // estrés
    { duration: "30s", target: 0 }, // enfriamiento
  ],
};

export default function () {
  const res = http.get("https://api.argly.com.ar/api/ipc");

  check(res, {
    "status es 200": (r) => r.status === 200,
    "respuesta < 500ms": (r) => r.timings.duration < 500,
  });

  sleep(1);
}
