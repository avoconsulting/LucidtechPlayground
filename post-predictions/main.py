import logging
import os
import traceback
from urllib import response

from las import Client
from numpy import var


logging.getLogger().setLevel(logging.INFO)


def handler(las_client, event, environ):
    """
    document_id = event['documentId']
    model_id = event.get('modelId', environ.get('MODEL_ID'))

    if not model_id:
        raise ValueError('A modelId is needed for prediction, input modelId directly or MODEL_ID to env')

    response = las_client.create_prediction(
        document_id=document_id,
        model_id=model_id,
        max_pages=event.get('maxPages', 1),
        auto_rotate=event.get('autoRotate', False),
    )
    """
    response = True
    return response


if __name__ == '__main__':
    las_client = Client()
    transition_id = os.environ['TRANSITION_ID']
    execution_id = os.environ['EXECUTION_ID']
    logging.info(f'Execute {execution_id} of transition {transition_id}')

    try:
        execution = las_client.get_transition_execution(transition_id, execution_id=execution_id)
        event = execution['input']
        logging.info(f'event: {event}')
        logging.info(f'Post prediction has succeeded')
        output = handler(las_client, event, environ=os.environ)
        las_client.update_transition_execution(
            transition_id=transition_id,
            execution_id=execution_id,
            status='succeeded',
            output=output,
        )
    except Exception:
        las_client.update_transition_execution(
            transition_id=transition_id,
            execution_id=execution_id,
            status='failed',
            error={
                'message': str(traceback.format_exc()),
            }
        )
        raise
