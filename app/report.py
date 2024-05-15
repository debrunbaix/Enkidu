import os
import datetime
import markdown
from weasyprint import HTML, CSS
from app.output_functions import output

#
# Function to put content on a list
#
def create_report_content(binary_info, file_path, assembly_code, fuzz_output):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report = []
    report.append(f"# Report for {binary_info['name']} at {today}\n")
    
    report.append("<div></div>")

    report.append("## Summary\n")
    report.append("- [General Information](#general-information)")
    report.append("- [Security of the Binary](#security-of-the-binary)")
    report.append("- [Strings](#strings)")
    report.append("- [Assembly Code](#assembly-code)")
    report.append("- [Code Analysis](#code-analysis)")
    report.append("- [Exploits](#exploits)")
    report.append("- [Credits](#credits)\n")

    report.append("<div></div>")

    report.append("## Enumeration\n")
    
    report.append("### Binary Information\n")
    report.append("<table>")
    report.append("<tr>")
    report.append("<th>File Name</th>")
    report.append("<th>Path</th>")
    report.append("<th>Format</th>")
    report.append("<th>Bit</th>")
    report.append("</tr>")
    report.append("<tr>")
    report.append(f"<td>{binary_info['name']}</td>")
    report.append(f"<td>{file_path}</td>")
    report.append(f"<td>{binary_info['format']}</td>")
    report.append(f"<td>{binary_info['bit']}-bit</td>")
    report.append("</tr>")
    report.append("</table>\n")

    report.append("### Security of the Binary\n")

    # Basic Security Features
    report.append("<table>")
    report.append("<tr><th colspan='4'>Basic Security Features</th></tr>")
    report.append("<tr>")
    report.append("<th>Linked</th>")
    report.append("<th>Stripped</th>")
    report.append("<th>RELRO</th>")
    report.append("<th>Canary</th>")
    report.append("</tr>")
    report.append("<tr>")
    report.append(f"<td>{binary_info['linked']}</td>")
    report.append(f"<td>{binary_info['stripped']}</td>")
    report.append(f"<td>{binary_info['relro']}</td>")
    report.append(f"<td>{binary_info['canary']}</td>")
    report.append("</tr>")
    report.append("</table>\n")

    # Advanced Security Mechanisms
    report.append("<table>")
    report.append("<tr><th colspan='3'>Advanced Security Mechanisms</th></tr>")
    report.append("<tr>")
    report.append("<th>NX</th>")
    report.append("<th>PIE</th>")
    report.append("<th>RPath</th>")
    report.append("</tr>")
    report.append("<tr>")
    report.append(f"<td>{binary_info['nx']}</td>")
    report.append(f"<td>{binary_info['pie']}</td>")
    report.append(f"<td>{binary_info['rpath']}</td>")
    report.append("</tr>")
    report.append("</table>\n")

    # Security Meta-Information
    report.append("<table>")
    report.append("<tr><th colspan='3'>Security Meta-Information</th></tr>")
    report.append("<tr>")
    report.append("<th>RunPath</th>")
    report.append("<th>Symbols</th>")
    report.append("<th>Fortify Source</th>")
    report.append("</tr>")
    report.append("<tr>")
    report.append(f"<td>{binary_info['runpath']}</td>")
    report.append(f"<td>{binary_info['symbols']}</td>")
    report.append(f"<td>{binary_info['fortify_source']}</td>")
    report.append("</tr>")
    report.append("</table>\n")

    
    report.append("### Strings\n")
    for string in binary_info.get('printed strings', []):
        report.append(f"- {string}")
    
    report.append("\n### Vulnerable Functions\n")
    if 'vulnerable_functions' in binary_info:
        for func in binary_info['vulnerable_functions']:
            report.append(f"- {func}")
    else:
        report.append("- No vulnerable functions identified\n")
    
    report.append("\n### Libraries\n")
    for lib in binary_info.get('library', []):
        report.append(f"- {lib}")

    report.append("\n### Assembly Code\n```assembly")
    for line in assembly_code:
        instruction_only = ' '.join(line.split()[1:])  # Skip the address part
        report.append(instruction_only)
    report.append("```\n")

    report.append("<div></div>")

    report.append("## Code Analysis\n")
    report.append("### Pseudo C Code\n")
    
    report.append("### ChatGPT Analysis\n")
    
    report.append("## Exploit\n")
    report.append("### Fuzzing")

    report.append("### Buffer Overflow\n")
    
    report.append("### Format String\n")
    
    report.append("## Credits\n")
    report.append("This report was generated using automated tools and the expert analysis of security researchers.\n")
    
    return "\n".join(report)

def markdown_to_html(md_text):
    return markdown.markdown(md_text)

def write_html_file(html_content, html_path):
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

def convert_html_to_pdf(html_path, pdf_path, css_path=None):
    html = HTML(html_path)
    css = CSS(css_path) if css_path else None
    html.write_pdf(pdf_path, stylesheets=[css] if css else None)

def generate_report(binary_info, file_path, report_folder, assembly_code, fuzz_output): 

    output('+', 0, 'Generating report.')

    # Définition des chemins pour les fichiers du rapport
    md_path = os.path.join(report_folder, f"{binary_info['name']}_report.md")
    html_path = os.path.join(report_folder, f"{binary_info['name']}_report.html")
    pdf_path = os.path.join(report_folder, f"{binary_info['name']}_report.pdf")
    css_path = 'app/styles/styles.css'  # Assurez-vous que le chemin vers le fichier CSS est correct

    # Création du contenu du rapport, écriture en Markdown, conversion en HTML et en PDF
    report_content = create_report_content(binary_info, file_path, assembly_code, fuzz_output)
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(report_content)
    
    output('+', 1, f'Markdown report created : {md_path}')

    html_content = markdown_to_html(report_content)
    write_html_file(html_content, html_path)

    output('+', 1, f'HTML report created : {html_path}')

    convert_html_to_pdf(html_path, pdf_path, css_path)

    output('+', 1, f'PDF report created : {pdf_path}')
