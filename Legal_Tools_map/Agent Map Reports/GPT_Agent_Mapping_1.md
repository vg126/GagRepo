# ICC Situations and Cases – taxonomy & document ID patterns

## 1\. Taxonomy structure

The ICC Legal Tools Database (LTD) uses a hierarchical tree for its collections. When the **International Criminal Court Documents** branch is expanded in the *Browse LTD Collections* panel, several high‑level collections appear, including **ICC Situations and Cases**, *Basic Documents*, *ICC Preparatory Works*, *ASP Documents* and others[\[1\]](https://www.legal-tools.org/). Selecting *ICC Situations and Cases* filters the database to documents relating to ICC proceedings and exposes a second level of classification:

| Level 2 branch | Description/role | Notes |
| :---- | :---- | :---- |
| **Preliminary Examinations (Not in Investigation)** | documents relating to preliminary examinations that have not yet led to formal investigations | clicking opens situations such as the *Comoros referral* etc. |
| **Main Situations** | the principal situations brought before the ICC; expanding this branch reveals situations such as *Afghanistan*, *Bangladesh/Myanmar*, *Burundi*, *Central African Republic*, *Côte d’Ivoire*, *Darfur (Sudan)*, *Democratic Republic of the Congo*, *Georgia*, *Kenya*, *Libya*, *Mali*, *Palestine*, *Philippines*, *Uganda* and others[\[1\]](https://www.legal-tools.org/). Each situation can be expanded further to reveal individual cases. | this category held most of the documents – roughly **49 k** records were returned when it was selected. |
| **Presidency and Appeals Chamber Review** | decisions of the ICC Presidency or Appeals Chamber on administrative matters or appellate issues | yields only a few hundred records. |

Within the **Main Situations** branch, each *situation* can be expanded to display *cases* (e.g., for the *Darfur, Sudan* situation the cases include **Harun & Ali Kushayb**, **Al‑Bashir**, **Hussain**, etc.). Selecting a case applies a further filter so that the results list only documents relating to that case. The top of the results list always displays a “crumb trail” showing the selected filters and the number of results[\[1\]](https://www.legal-tools.org/).

## 2\. Document inventory & patterns

### Overall counts

Selecting **ICC Situations and Cases** returned roughly **50 k documents** across all situations[\[1\]](https://www.legal-tools.org/). Applying the *Main Situations* filter reduced the dataset slightly to \~49 k documents. When individual situations were selected, counts dropped significantly; for example, **Situation in the Islamic Republic of Afghanistan** returned **295 documents**[\[2\]](https://www.legal-tools.org/). Counts for other situations ranged from a few hundred (e.g., *Burundi*) to several thousand (e.g., *Democratic Republic of the Congo*).

### Sample documents

Each result in the list displays the document title, date, issuing body and a link whose path ends with /doc/{ID}/. The ID is a short alphanumeric code (usually six–eight characters). Many titles contain ICC case numbers. Opening a document page reveals a metadata table with a **Persistent URL**, **Title**, **External identifier** (ICC case number), **Content type**, source, date created and a link to the underlying PDF[\[3\]](https://www.legal-tools.org/doc/bab8kl/). The table below summarises sample documents extracted during this exploration:

| Situation / case | Document ID (Persistent URL) | Title / document type (abridged) | External identifier & notes |
| :---- | :---- | :---- | :---- |
| *Situation in the Islamic Republic of Afghanistan* | **a076io** (https://legal‑tools.org/doc/a076io/) | *Prosecution reply to “Response to Prosecution appeal …”* (appeal against Article 18(2) decision) | **ICC‑02/17‑204** – pre‑trial appeal decision; illustrates the pattern ICC‑02/17‑XXX where **02/17** is the situation code for Afghanistan[\[2\]](https://www.legal-tools.org/). |
| *Situation in the Islamic Republic of Afghanistan* | **bab8kl** (https://legal‑tools.org/doc/bab8kl/) | *Decision on the Prosecutor’s request for leave to reply* | **ICC‑02/17‑206** – decision by the Appeals Chamber; metadata page shows source type “Judicial body” and notes that the document is a “Type of Judicial document”[\[3\]](https://www.legal-tools.org/doc/bab8kl/). |
| *Main Situations – Libya* | **v0r0673j** (https://legal‑tools.org/doc/v0r0673j/) | *Decision on the “Defence request for leave to appeal”* (Libya appeal) | **ICC‑01/11‑01/11‑???** (not all identifiers visible in list); pattern shows situation code **01/11** for Libya cases[\[1\]](https://www.legal-tools.org/). |
| *Situation in the Saif Suleiman Sneidel case (Libya)* | **i3dxot7g** (https://legal‑tools.org/doc/i3dxot7g/) | *Public redacted version of decision granting the Prosecution’s second application to unseal the warrant of arrest for Saif Suleiman Sneidel* | **ICC‑01/11‑01/20‑26‑Red** – external identifier contains situation **01/11**, case **01/20** and document number **26**, suffixed with “Red” for a redacted version[\[3\]](https://www.legal-tools.org/doc/bab8kl/). |

These examples illustrate that the document IDs are short, seemingly random codes, while the **external identifier** follows ICC numbering conventions and encodes the situation number and case number. Titles often reproduce the external identifier, which helps align documents to specific cases.

## 3\. External identifier patterns

ICC case numbers follow systematic conventions:

* **ICC‑SS/PP‑CC/DD** – the first two numbers (SS) designate the situation (e.g., **02/17** for Afghanistan, **01/11** for Libya). The next two numbers (PP) denote the specific case within the situation (e.g., **01/20** in the *Saif Suleiman Sneidel* warrant). Additional elements (e.g., “‑Red” for redacted versions or appended letters such as “‑A” for appeal filings) indicate document type or version[\[3\]](https://www.legal-tools.org/doc/bab8kl/).

* **Situation‑only documents** (e.g., Article 18 decisions) use the pattern **ICC‑SS/PP‑XXX** where only the situation code appears (e.g., ICC‑02/17‑204). These documents apply to the situation rather than a particular accused.[\[2\]](https://www.legal-tools.org/).

* **Preliminary examination documents** use more general identifiers, but when an investigation opens they follow the same format.

The presence of the ICC case number in document titles makes it possible to map documents to situations and cases even without opening each page.

## 4\. Systematic access insights

1. **Navigating the taxonomy:** Use the *Browse LTD Collections* panel. Under **International Criminal Court Documents** select **ICC Situations and Cases** and then choose from *Preliminary Examinations*, *Main Situations* or *Presidency and Appeals Chamber Review*. Expanding **Main Situations** reveals a list of situations; each has a plus icon to further expand cases[\[1\]](https://www.legal-tools.org/).

2. **Filtering by situation/case:** Clicking a situation applies a filter and shows a crumb trail indicating the path (e.g., *ICC Situations and Cases → Main Situations → Situation in Afghanistan*). The results count at the top shows how many documents the filter returns (Afghanistan: 295 documents[\[2\]](https://www.legal-tools.org/)). You can clear individual filters by clicking the **×** on the crumb.

3. **Harvesting documents:** Each result row contains a link to the document (/doc/{ID}/). For systematic harvesting, iterate through pages (20 results per page) and capture the IDs and associated case numbers. The metadata page (INFO tab) provides additional fields such as the external identifier, source, language, case name and PDF link[\[3\]](https://www.legal-tools.org/doc/bab8kl/).

4. **Bulk patterns:**

5. The **Main Situations** branch holds the vast majority of documents (\~49 k). The **Preliminary Examinations** and **Presidency/Appeals Review** branches have significantly fewer records.

6. Situation‑specific counts vary, with long‑standing situations (e.g., **Democratic Republic of the Congo**, **Darfur (Sudan)**) containing thousands of documents, while newer or less active situations have only hundreds.

## 5\. Technical patterns

* **URL structure:** Every document has a **persistent URL** of the form https://www.legal-tools.org/doc/{ID}/, where {ID} is a base‑62 alphanumeric string. The PDF file is stored on the ICC’s main web site and can be retrieved via the CourtRecords directory (e.g., https://www.icc-cpi.int/sites/default/files/CourtRecords/0902ebd180c4f747.pdf)[\[3\]](https://www.legal-tools.org/doc/bab8kl/).

* **Metadata fields:** The INFO tab of each document includes fields for *Persistent URL*, *Title*, *External identifier*, *Content type*, *Source*, *Organisation/state of source*, *Date created*, *Authoritative language* and *Case name*. These fields allow programmatic retrieval and mapping across situations[\[3\]](https://www.legal-tools.org/doc/bab8kl/).

* **Identifier relationships:** The random ID in the persistent URL does **not** encode the situation; it functions purely as a database key. The external identifier encodes the situation and case numbers, allowing researchers to correlate documents with ICC proceedings.

## Conclusion

The **ICC Situations and Cases** branch of the ICC Legal Tools Database is structured in a clear hierarchy: high‑level categories for preliminary examinations, main situations and appeals; individual situations; and, at the next level, specific cases. Document IDs are random alphanumeric keys used in the URL, while the **external identifiers** follow predictable ICC case numbering conventions (e.g., ICC‑02/17‑204). The database’s filtering interface, counts and metadata tables make it possible to systematically harvest document IDs and map them to specific situations and cases[\[2\]](https://www.legal-tools.org/)[\[3\]](https://www.legal-tools.org/doc/bab8kl/).

---

[\[1\]](https://www.legal-tools.org/) [\[2\]](https://www.legal-tools.org/) ICC Legal Tools Database

[https://www.legal-tools.org/](https://www.legal-tools.org/)

[\[3\]](https://www.legal-tools.org/doc/bab8kl/) ICC Legal Tools Database | Decision on the Prosecutor’s request for leave to reply

[https://www.legal-tools.org/doc/bab8kl/](https://www.legal-tools.org/doc/bab8kl/)