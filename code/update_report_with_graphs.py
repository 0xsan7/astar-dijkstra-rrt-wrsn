from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

doc = SimpleDocTemplate("../results/WRSN_RESEARCH_REPORT_COMPLETE.pdf", pagesize=letter,
                       rightMargin=0.75*inch, leftMargin=0.75*inch,
                       topMargin=0.75*inch, bottomMargin=0.75*inch)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=18, spaceAfter=12, alignment=1)
heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=14, spaceAfter=10)

story = []

# Title
story.append(Paragraph("Comparative Analysis of Pathfinding Algorithms for Mobile Charging Vehicle Routing", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Santiago Jerald | NIT Goa | Mentor: Dr. S Mini", styles['Normal']))
story.append(Paragraph("August 2026 - UPDATED WITH COMPLETE DIJKSTRA TESTING", styles['Normal']))
story.append(Spacer(1, 0.3*inch))

# Update Notice
story.append(Paragraph("<b>UPDATE NOTICE</b>", heading_style))
story.append(Paragraph("This report now includes complete Dijkstra algorithm testing on all network sizes (10, 25, 50, 100 nodes). Previous version limited Dijkstra to 10-25 nodes due to computational constraints.", styles['Normal']))
story.append(Spacer(1, 0.3*inch))

# Graph 1
story.append(Paragraph("5.1 Path Length - No Obstacles (ALL ALGORITHMS, ALL SIZES)", heading_style))
story.append(Image("../results/graphs/1_path_length_no_obstacles.png", width=6*inch, height=3.5*inch))
story.append(Paragraph("A* maintains shortest paths across all network sizes. Dijkstra comparable on small networks. Complete data now available for 50 and 100 nodes.", styles['Normal']))
story.append(Spacer(1, 0.3*inch))
story.append(PageBreak())

# Graph 2
story.append(Paragraph("5.2 Path Length - With Obstacles (ALL ALGORITHMS, ALL SIZES)", heading_style))
story.append(Image("../results/graphs/2_path_length_with_obstacles.png", width=6*inch, height=3.5*inch))
story.append(Paragraph("A* shows robust obstacle handling. RRT most impacted. Dijkstra data now complete for all scales.", styles['Normal']))
story.append(Spacer(1, 0.3*inch))
story.append(PageBreak())

# Graph 3
story.append(Paragraph("5.3 Computation Time (ALL ALGORITHMS, ALL SIZES)", heading_style))
story.append(Image("../results/graphs/3_computation_time_no_obstacles.png", width=6*inch, height=3.5*inch))
story.append(Paragraph("<b>KEY FINDING:</b> Dijkstra at 50 nodes = 25,829ms | At 100 nodes = 7,310-45,695ms. A* remains ~30ms at 100 nodes.", styles['Normal']))
story.append(Spacer(1, 0.3*inch))
story.append(PageBreak())

# Graph 4
story.append(Paragraph("5.4 Computation Time With Obstacles (ALL ALGORITHMS, ALL SIZES)", heading_style))
story.append(Image("../results/graphs/4_computation_time_with_obstacles.png", width=6*inch, height=3.5*inch))
story.append(Paragraph("Complete Dijkstra data confirms computational ceiling. A* is practical choice for networks beyond 25 nodes.", styles['Normal']))
story.append(Spacer(1, 0.5*inch))

# Conclusion
story.append(PageBreak())
story.append(Paragraph("7 Conclusion - Updated with Complete Data", heading_style))
story.append(Paragraph("Complete testing on all network sizes (10-100 nodes) confirms A* algorithm superiority for WRSN routing. Dijkstra's computational requirements, now empirically confirmed at all scales, fundamentally limit real-world applicability. RRT remains viable for speed-prioritized applications.", styles['Normal']))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<i>Report generated: August 5, 2026 with complete algorithm comparison</i>", styles['Normal']))
story.append(Paragraph("<b>Code available at:</b> https://github.com/0xsan7/astar-dijkstra-rrt-wrsn", styles['Normal']))

doc.build(story)
print("✅ Updated PDF created: WRSN_RESEARCH_REPORT_COMPLETE.pdf")
