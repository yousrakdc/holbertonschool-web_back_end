/* eslint-disable */
export default function guardrail(mathFunction) {
    const queue = [];
    queue.push(
      (() => {
        try {
          return mathFunction();
        } catch (error) {
          return `${error}`;
        }
      })(),
      'Guardrail was processed',
    );
    return queue;
  }