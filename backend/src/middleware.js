import * as Sentry from "@sentry/node";

export function errorHandler(err, req, res, next) {
  Sentry.captureException(err);
  console.info(err.message);
  if (typeof err.statusCode == "undefined") {
    err.statusCode = 500;
  }
  res.status(err.statusCode).send({
    error: err.message,
  });
  return;
}
