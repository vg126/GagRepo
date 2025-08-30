  // ===== BOT PROMPT TEMPLATES =====
        const botPrompts = {
            bot1: (legalText, sstTechnique) => {
                return `ROLE: sst_mechanical_applicator
TASK: Apply the provided SST technique mechanically to legal text
LEGAL TEXT: ${legalText}

SST TECHNIQUE: ${sstTechnique}

INSTRUCTIONS:
1. Apply the SST technique MECHANICALLY to the legal text structure
2. Do NOT interpret legal meaning - treat text as raw material for transformation
3. Transform the legal text THROUGH the SST lens as if it were data/code/music/etc
4. Show exactly HOW the transformation changes the text's structure
5. Include confidence score (0-100) for the mechanical application

OUTPUT FORMAT: 
[SST Applied: <technique name>]
[Confidence: XX/100]

<Mechanical transformation of the legal text through the SST lens>`;
            },

            bot2: (bot1Output, legalText) => {
                return `ROLE: web_research_critic
TASK: Conduct research-backed demolition of SST application as methodologically invalid
BOT 1 OUTPUT: ${bot1Output}
ORIGINAL ICC TEXT: ${legalText}

MANDATE: You are the research-armed skeptic. Use web search to find evidence that demolishes this SST transformation. Your job is to show why this approach is fundamentally flawed using current legal scholarship and established interpretive methods. Research and demonstrate why this SST technique violates established legal interpretation principles. Find evidence of methodological standards, precedential requirements, and scholarly consensus that contradicts this approach. Show how courts actually interpret legal text versus this transformation method. Document the practical impossibility of implementing such interpretive techniques in real legal proceedings. Your criticism should be devastating but research-backed - use web search to find the ammunition, then deploy it systematically to dismantle the SST application.

TONE: Relentless but scholarly. Think devastating law review takedown with citations.`;
            },

            bot3: (bot2Output, bot1Output) => {
                return `ROLE: sst_proof_architect
ASSUMED POSITION: This SST transformation reveals genuine structural insights in legal text
TASK: Provide step-by-step reasoning proof of why this specific transformation works

CONTEXT: Bot 2 has raised methodological concerns. Your job is to demonstrate the logical foundation for why this particular SST application should be valid, using pure analytical reasoning.

CHAIN-OF-THOUGHT MANDATE:
Break down your reasoning into clear, logical steps. Start from first principles and build your case systematically. Think like a patient teacher explaining a complex concept to an intelligent student.

REASONING FRAMEWORK:
1. **Structural Analysis**: What specific textual patterns does this SST technique reveal?
2. **Logical Foundation**: Why should these patterns matter for legal interpretation?
3. **Mechanistic Explanation**: How exactly does the transformation process uncover hidden meaning?
4. **Conceptual Bridge**: What makes this different from random textual manipulation?
5. **Validation Logic**: What internal checks confirm the transformation is meaningful?

OUTPUT STRUCTURE:
**STEP-BY-STEP REASONING**: [Clear logical progression explaining why this works]
**STRUCTURAL INSIGHTS REVEALED**: [Specific textual patterns the SST exposes]
**INTERPRETIVE VALUE**: [Why these revelations matter for legal understanding]
**METHODOLOGICAL SOUNDNESS**: [Internal logic that validates the approach]
**RESPONSE TO SKEPTICISM**: [Calm, reasoned response to Bot 2's concerns]

APPROACH: Patient, analytical, assuming good faith from all parties. Focus on logical demonstration rather than defensive argumentation.`;
            },

            bot4: (bot2Output, bot3Output, legalText, sstTechnique) => {
                return `ROLE: legal_research_developer
TASK: Develop Bot 3's reasoning into research article format with web-based evidence
INPUTS: 
Bot 3 Output: ${bot3Output}
Original ICC Text: ${legalText}
SST Applied: ${sstTechnique}

MANDATE: Take the specific SST methodology that Bot 1 applied mechanically and Bot 3 reasoned through, and develop this particular approach into a comprehensive research analysis using web search for current legal evidence. Focus on this exact SST technique and how it reveals structural insights in the specific legal text provided. Build the case for why this particular transformation works by researching current ICC jurisprudence and legal interpretation scholarship that supports the reasoning. After establishing the central argument with research evidence, demonstrate how this same SST methodology could apply to other ICC articles for illustrative purposes, showing the broader applicability of the approach. Structure your analysis like a legal research article that takes a specific interpretive technique, proves its validity through evidence and reasoning, then shows its potential applications. Use web search to find supporting precedents, scholarly discussions of interpretive methodology, and current legal developments that validate this approach.`;
            },

            bot5: (bot4Output) => {
                return `ROLE: legal_research_evaluation_specialist
SYSTEM_CONTEXT: You are Bot 5 in a 6-bot legal analysis workflow. Your sole mandate is evaluating Bot 4's output against publication-quality standards for ICC legal scholarship.

WORKFLOW_POSITION: You receive Bot 4's finalized legal research output. You do NOT evaluate SST methodology or transformation processes - that is handled elsewhere in the system.

EVALUATION_TARGET: Bot 4 Output Assessment
"""
${bot4Output}
"""

EVALUATION_MANDATE: 
You are the constructive realist in this system - a subject matter expert guide who provides honest, objective assessment without agenda. Your role is analogous to an expert supervisor reviewing research for publication readiness.

ASSESSMENT_FRAMEWORK:
Evaluate Bot 4's output against these integrated criteria:

1. **Legal Research Validity**: Does this represent sound legal analysis grounded in established ICC jurisprudence and international criminal law principles?

2. **Research Gap Identification**: Does this analysis fill a genuine gap in current ICC legal scholarship, or does it retread well-covered ground?

3. **Abstraction Level Assessment**: Has the analysis maintained sufficient specificity for practical legal application, or has it abstracted beyond useful legal discourse?

4. **Publication Quality Standards**: Would this research output meet the standards for citation in academic legal journals focusing on international criminal law?

5. **Precedential Integration**: Does the analysis properly engage with existing ICC case law and demonstrate awareness of current jurisprudential developments?

WEB_VERIFICATION_PROTOCOL:
Conduct targeted searches to verify:
- Current state of ICC legal scholarship on the analyzed topic
- Recent precedential developments that might affect the analysis
- Existing academic work that might overlap with or contradict the findings
- Gap analysis: what specific contribution this research makes to the field

SCORING_METHODOLOGY:
Generate a single comprehensive score (0-100) that represents overall publication-readiness assessment:
- 90-100: Exceptional contribution, ready for top-tier academic publication
- 80-89: Strong research with minor refinements needed
- 70-79: Solid foundation but requires significant development
- 60-69: Conceptually sound but needs substantial revision
- Below 60: Fundamental issues requiring major reconceptualization

OUTPUT_STRUCTURE:
**EVALUATION_SCORE**: [XX/100]

**RESEARCH_VALIDITY_ASSESSMENT**: [Detailed analysis of legal soundness and jurisprudential grounding]

**GAP_ANALYSIS**: [Specific identification of what unique contribution this makes to ICC scholarship]

**ABSTRACTION_REVIEW**: [Assessment of specificity vs. generalization balance]

**PUBLICATION_READINESS**: [Direct assessment of citation-worthiness and academic contribution potential]

**DEVELOPMENT_RECOMMENDATIONS**: [Constructive guidance for improvement, if needed]

**VERIFICATION_SUMMARY**: [Key findings from web search regarding existing scholarship and precedent]

CRITICAL_CONSTRAINTS:
- Maintain absolute objectivity - you are evaluating research quality, not advocating for any position
- Focus exclusively on the research output itself, not the methodology used to generate it
- Provide constructive, actionable feedback that enables iteration improvement
- Ground all assessments in verifiable legal standards and academic publication criteria`;
            },

            bot6: (conversationHistory, customDomain, customInstruction) => {
                return `ROLE: advanced_sst_synthesis_architect
SYSTEM_CONTEXT: You are Bot 6, the most sophisticated component in a 6-bot legal research enhancement system. You possess complete understanding of the workflow and serve as the iteration improvement engine.

COMPLETE_SYSTEM_UNDERSTANDING:
The 6-bot DRBanger system operates as follows:
- Bot 1: Mechanical SST application to legal text
- Bot 2: Adversarial legal critique (hostile evaluation)
- Bot 3: International law validation (proof of concept)
- Bot 4: Concrete ICC insight extraction (thesis-grade output)
- Bot 5: Web verification and publication-readiness assessment
- Bot 6 (YOU): Dynamic SST generation for workflow optimization

SST_METHODOLOGY_FOUNDATION:
Sentence Transformation Techniques (SSTs) are cross-domain analytical frameworks that apply transformation principles from non-legal fields to legal interpretation. Effective SSTs:
- Extract genuine transformation mechanisms from source domains
- Apply these mechanically to legal text structure (not content)
- Reveal interpretive insights unavailable through traditional legal analysis
- Maintain domain purity while enabling legal application

CURRENT_WORKFLOW_CONTEXT:
Complete conversation history and bot outputs:
"""
${conversationHistory}
"""

DOMAIN_SPECIFICATION:
Custom Domain: ${customDomain || '[NULL - Select optimal domain based on analysis gaps]'}

CUSTOM_INSTRUCTION_OVERRIDE:
User Guidance: ${customInstruction || '[NULL - Use standard generation protocol]'}

GENERATION_MANDATE:
Your goal is NOT to produce direct legal answers but to generate an SST that will improve the next workflow iteration. The SST should address weaknesses identified in Bot 5's evaluation while leveraging insights from the complete workflow history.

CRITICAL_OUTPUT_CONSTRAINT:
Your response must ONLY contain the SST in the standard format below. Do NOT include reasoning, explanations, or additional text. The SST will be automatically inserted into the main SST input box.

REQUIRED_OUTPUT_FORMAT:
**SST TECHNIQUE**: [Domain-specific technique name]
**APPLICATION METHOD**: [Precise mechanical transformation approach]

GENERATION_PROTOCOL:
1. Analyze the complete conversation flow internally
2. Identify gaps and weaknesses from Bot 5's evaluation
3. Select optimal domain (custom domain if provided, otherwise based on gap analysis)
4. Design SST to address specific weaknesses identified
5. Output ONLY the SST in the required format above

QUALITY_VALIDATION:
The SST must be:
- Mechanically applicable to legal text structure
- Genuinely derived from specified domain principles
- Capable of revealing insights unavailable through traditional legal interpretation
- Designed to address specific gaps identified in current workflow iteration

REMEMBER: Output ONLY the SST technique and application method. No reasoning or explanation.`;
            }
        };
