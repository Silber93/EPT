# Dataset Card for EPT

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://teacherluke.co.uk/
- **Repository:** https://github.com/Silber93/EPT.git
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The English Podcast Transcript dataset is an English-language dataset of transcripts and summaries of podcasts designed to help listeners learn British English and improve it, and is provided as a small dataset for general tasks.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

English (UK)

## Dataset Structure

### Data Instances

A typical data point comprises the title of the podcast episode, the date of publish and 'simple_text' containing the the transcript. the data is saved as a csv file, and every feature presented as a column.
example:

```
{
    'ep_name': '70. Language and Music (with Francis Duncan)',
    'ep_date': '14/10/2011',
    'simple_text': 'What are the similarities between ...'
}
```


### Data Fields

- ep_name: a string of the text title.
- ep_date: a string of the publish date.
- simple_text: a string of the transcript, where every column is separated by TAB.

### Data Splits

Data is not splitted.

## Dataset Creation

### Curation Rationale

The data was extracted from the podcast webpage and cleaned for the purposes of the HuggingFace project.

### Source Data

#### Initial Data Collection and Normalization

The data was obtained by creating a crawler that extracted podcast urls from the transcript archive (http://teacherluke.co.uk/episodes-with-transcripts/). Afterwards, for each url extracted we ran a crawler that extracted the data into txt files. In the last stage, we dumped files containing under 20 lines of text assuming whose files are likely to be summaries rather than transcripts.

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]
