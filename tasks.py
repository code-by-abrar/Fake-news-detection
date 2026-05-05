from crewai import Task

def create_tasks(researcher, editor, claim):
    # Task 1 for Researcher
    research_task = Task(
        description=f'Verify this claim: "{claim}". \n'
                    f'2. Use "Wikipedia_Search" for context on entities involved.\n'
                    f'3. Use "Internet_Search" for latest news and multiple perspectives.\n'
                    f'Gather the raw truth from multiple reliable sources.',
        expected_output='A detailed summary of findings, specifically citing fact-checks if found, and listing sources.',
        agent=researcher
    )

    # Task 2 for Editor
    editing_task = Task(
        description='Take the research findings and write a final fact-check report. The report MUST include:\n'
                    '1. TRUTH SCORE: A number from 0 to 100 (where 0 is a total lie and 100 is absolute truth).\n'
                    '2. VERDICT: (True/False/Misleading/Unverified)\n'
                    '3. SUMMARY: A concise explanation of why.\n'
                    '4. SOURCES: List the references found.',
        expected_output='A professionally formatted fact-check report starting with "TRUTH SCORE: [number]".',
        agent=editor
    )

    return [research_task, editing_task]