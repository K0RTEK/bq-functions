import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def job_classification(job_id: str, job_type: str, query: str, user_email: str) -> str:
    job_id = is_none(job_id)
    job_type = is_none(job_type)
    query = is_none(query)
    user_email = is_none(user_email)

    if job_id.startswith('materialized_view_refresh_'):
        return 'materialized_view_refresh'
    elif job_id.startswith('scheduled_query_'):
        return 'scheduled_query'
    elif job_id.startswith('script_job_'):
        return 'script_job'
    elif job_id.startswith('bquxjob_'):
        return 'bq user interface'
    elif job_id.startswith('bqjob_'):
        return 'bigquery load or copy job - somewhat unclear'
    elif job_id.startswith('dataform-gcp'):
        return 'Dataform job'
    elif job_id.startswith('clouddq-'):
        return 'Cloud Composer job'
    elif job_id.startswith('job_') and job_type == 'EXTRACT':
        return 'BQ UI data export to Google Drive'
    elif job_id.startswith('adwords_'):
        return 'adwords'
    elif job_id.startswith('google_ads_'):
        return 'google_ads'
    elif job_id.startswith('merchant_center_'):
        return 'merchant_center'
    elif job_id == '123456-0000-1234-baa9-1234463245':
        return 'billing data transfer'
    elif job_id.startswith('bqts_'):
        return 'Dataset Copy in Data Transfers'
    elif job_id.startswith('your ga account number'):
        return 'google analytics'
    elif job_id.startswith('some_number_and_then_the_word_analytics') or 'your_account_number' in job_id:
        return 'google analytics'
    elif user_email == 'for-script@fsk-analytics.iam.gserviceaccount.com':
        return 'rlc_services'
    elif job_id.startswith('sheets_dataconnector_'):
        return 'sheets_dataconnector'
    elif job_id.startswith('job-exponea'):
        return 'job-exponea'
    elif job_id.startswith('job_'):
        return 'lookerstudio job'
    elif query.startswith('/* {"app":"dbt"'):
        return 'dbt job'
    elif user_email == 'some_user_or_serviceaccount@bla.iam.gserviceaccount.com':
        return 'job based on a certain user email'
    elif re.match(r'^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$', job_id):
        return 'python bq client jobs'
    else:
        return 'unknown'
