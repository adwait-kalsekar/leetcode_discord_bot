import leetcode

leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb2NpYWxhY2NvdW50X3NvY2lhbGxvZ2luIjp7ImFjY291bnQiOnsiaWQiOm51bGwsInVzZXJfaWQiOm51bGwsInByb3ZpZGVyIjoiZ29vZ2xlIiwidWlkIjoiMTEyNjA5MTc1MTI5NDI3MjMyMTMzIiwibGFzdF9sb2dpbiI6bnVsbCwiZGF0ZV9qb2luZWQiOm51bGwsImV4dHJhX2RhdGEiOnsiaWQiOiIxMTI2MDkxNzUxMjk0MjcyMzIxMzMiLCJlbWFpbCI6ImthbHNla2FyYWR3YWl0QGdtYWlsLmNvbSIsInZlcmlmaWVkX2VtYWlsIjp0cnVlLCJuYW1lIjoiQWR3YWl0IEthbHNla2FyIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BTFYtVWpWbU1FYkpkSmxweHZZMXlLRjIzZXQ0eG9kbWJUdkRqcEkxMFJTRVBsSXU9czk2LWMifX0sInVzZXIiOnsiaWQiOm51bGwsInBhc3N3b3JkIjoiIWc4aGJTWHBaa0FGUFZnbFVBN1BPaXZxajU3bzBNS3pMMFNnbjdpWEQiLCJsYXN0X2xvZ2luIjpudWxsLCJpc19zdXBlcnVzZXIiOmZhbHNlLCJ1c2VybmFtZSI6IiIsImZpcnN0X25hbWUiOiIiLCJsYXN0X25hbWUiOiIiLCJlbWFpbCI6ImthbHNla2FyYWR3YWl0QGdtYWlsLmNvbSIsImlzX3N0YWZmIjpmYWxzZSwiaXNfYWN0aXZlIjp0cnVlLCJkYXRlX2pvaW5lZCI6IjIwMjQtMDItMjRUMTg6MjY6MDIuOTc5WiJ9LCJzdGF0ZSI6eyJuZXh0IjoiLyIsInByb2Nlc3MiOiJsb2dpbiIsInNjb3BlIjoiIiwiYXV0aF9wYXJhbXMiOiIifSwiZW1haWxfYWRkcmVzc2VzIjpbeyJpZCI6bnVsbCwidXNlcl9pZCI6bnVsbCwiZW1haWwiOiJrYWxzZWthcmFkd2FpdEBnbWFpbC5jb20iLCJ2ZXJpZmllZCI6dHJ1ZSwicHJpbWFyeSI6dHJ1ZX1dLCJ0b2tlbiI6eyJpZCI6bnVsbCwiYXBwX2lkIjoxLCJhY2NvdW50X2lkIjpudWxsLCJ0b2tlbiI6InlhMjkuYTBBZkJfYnlDamFTWWFDd3Ruc2lFYkg2dHNLMGlQUXQ4d1ozbEkySUdNLVVRS3N0ZmJyMEVJcmZzUFB3ZkJ4Yl9iRjhLdkVmSHlPbmhFdGJRR0VIb0Z5Sm16ZElJaVFLM0s3VTdXV3RYWmxqcmJNaXdWYmt5Vkdmd3dWVndyNll6aVVRekpjNFBFX3B3SFR0NVhCQ292TzN4bTI0blpvTm5rSV9XWmFDZ1lLQWVFU0FSRVNGUUhHWDJNaTd2SXRZT2tMenh0d1Z6aFNzVUlwWEEwMTcxIiwidG9rZW5fc2VjcmV0IjoiIiwiZXhwaXJlc19hdCI6IjIwMjQtMDItMjRUMTk6MjY6MDEuODY3WiJ9fSwiX3Bhc3N3b3JkX3Jlc2V0X2tleSI6ImMyd2QwOC1iZmEzMGRiZDRlZDdjZGYzZGYyYTRmOTYzNTFmODA0NyIsIl9hdXRoX3VzZXJfaWQiOiIyOTk3NjQ5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NjJiM2M0MmZhZmUxMGYyNWY5OTg1YWViODQwY2U3YTgyNjA1YzhiY2E5NzdlN2E0YTRmNzIwYjg0MzBiZjQ0IiwiaWQiOjI5OTc2NDksImVtYWlsIjoia2Fsc2VrYXJhZHdhaXRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJmYWNlYm9sdCIsInVzZXJfc2x1ZyI6ImZhY2Vib2x0IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTcwODc5OTIzMiwiaXAiOiIxMjguNi4zNi4yMTEiLCJpZGVudGl0eSI6IjI0ZTg3ZTVmMTU2YWI0OGM1YmI1NTllNGMxNjUyMjM0Iiwic2Vzc2lvbl9pZCI6NTYzMTQwNTQsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.25TpHOWBKsr9xYsHjhJ7iC-EB5LE-UaqIs4b78w8p8w"
csrf_token = "dRFn5uVgDMh3v60YWMmlIvy2q6qyqQrXwKiUBWbpVzHFttUGWVLhxG8rW2siZSeB"
configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance =leetcode.DefaultApi(leetcode.ApiClient(configuration))
graphql_request = leetcode.GraphqlQuery(
query="""
     {
       user {
            username
            isCurrentUserPremium
         }
     }
     """,
variables=leetcode.GraphqlQueryVariables(),
)
print(api_instance.graphql_post(body=graphql_request))

api_response=api_instance.api_problems_topic_get(topic="algorithms")
solved_questions=[]
for questions in api_response.stat_status_pairs:
    if questions.status=="ac":
       solved_questions.append(questions.stat.question__title)
print(solved_questions)
print("Total number of solved questions ",len(solved_questions))